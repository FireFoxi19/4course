using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Converter
{
    class Controller
    {

        int _pIn = 10;
        int _pOut = 16;
        const int _accuracy = 10;
        private State _state;

        public HistoryController history = new HistoryController();
        public enum State { Edit, Converted }
        internal State _State { get => _state; set => _state = value; }
        public int Pin { get => _pIn; set => _pIn = value; }
        public int Pout { get => _pOut; set => _pOut = value; }

        public Controller()
        {
            _State = State.Edit;
            Pin = _pIn;
            Pout = _pOut;
        }

        public EditorController editor = new EditorController();

        public string doCmnd(int j)
        {
            if (j == 19)
            {
                double var = ConvertControllerPDecimal.Dval(editor.getNumber(), (Int16)Pin);
                string result = ConvertControllerDecimalP.Do(var, (Int32)Pout, Accuracy());
                _State = State.Converted;
                history.addRecord(Pin, Pout, editor.getNumber(), result);
                return result;
            }
            else
            {
                _State = State.Edit;
                return editor.doEdit(j);
            }
        }


        private int Accuracy()
        {
            return (int)Math.Round(editor.acc() * Math.Log(Pin) / Math.Log(Pout) + 0.5);
        }
    }
    public class ConvertControllerDecimalP
    {

        public static string Do(double n, int p, int c)
        {
            if (p < 2 || p > 16)
                throw new IndexOutOfRangeException();
            if (c < 0 || c > 10)
                throw new IndexOutOfRangeException();

            long leftSide = (long)n;

            double rightSide = n - leftSide;
            if (rightSide < 0)
                rightSide *= -1;

            string leftSideString = IntP(leftSide, p);
            string rightSideString = DblP(rightSide, p, c);

            return leftSideString + (rightSideString == String.Empty ? "" : ".") + rightSideString;
        }

        public static char IntСhar(int d)
        {
            if (d > 15 || d < 0)
            {
                throw new IndexOutOfRangeException();
            }
            string allSymbols = "0123456789ABCDEF";
            return allSymbols.ElementAt(d);
        }

        public static string IntP(long n, int p)
        {
            if (p < 2 || p > 16)
                throw new IndexOutOfRangeException();
            if (n == 0)
                return "0";
            if (p == 10)
                return n.ToString();

            bool isNegative = false;
            if (n < 0)
            {
                isNegative = true;
                n *= -1;
            }

            string buf = "";
            while (n > 0)
            {
                buf += IntСhar((int)n % p);
                n /= p;
            }

            if (isNegative)
                buf += "-";

            char[] chs = buf.ToCharArray();
            Array.Reverse(chs);
            return new string(chs);
        }

        public static string DblP(double n, int p, int c)
        {
            if (p < 2 || p > 16)
                throw new IndexOutOfRangeException();
            if (c < 0 || c > 10)
                throw new IndexOutOfRangeException();

            string pNumber = String.Empty;
            for (int i = 0; i < c; i++)
            {
                pNumber += IntСhar((int)(n * p));
                n = n * p - (int)(n * p);
            }
            return pNumber;
        }
    }
    public class ConvertControllerPDecimal
    {

        public static double Dval(string p_num, int p)
        {
            if (p < 2 || p > 16)
                throw new IndexOutOfRangeException();

            double buf = 0d;
            if (p_num.Contains("."))
            {
                string[] lr = p_num.Split('.');
                if (lr[0].Length == 0)
                    throw new Exception();
                char[] chs = lr[0].ToCharArray();
                Array.Reverse(chs);
                for (int i = 0; i < chs.Length; i++)
                {
                    if (Char_to_num(chs[i]) > p)
                        throw new Exception();
                    buf += Char_to_num(chs[i]) * Math.Pow(p, i);
                }
                char[] chsr = lr[1].ToCharArray();
                for (int i = 0; i < chsr.Length; i++)
                {
                    if (Char_to_num(chsr[i]) > p)
                        throw new Exception();
                    buf += Char_to_num(chsr[i]) * Math.Pow(p, -(i + 1));
                }
            }
            else
            {
                char[] chs = p_num.ToCharArray();
                Array.Reverse(chs);
                for (int i = 0; i < chs.Length; i++)
                {
                    if (Char_to_num(chs[i]) > p)
                        throw new Exception();
                    buf += Char_to_num(chs[i]) * Math.Pow(p, i);
                }
            }
            return buf;
        }

        public static double Char_to_num(char ch)
        {
            string allNums = "0123456789ABCDEF";
            if (!allNums.Contains(ch))
                throw new IndexOutOfRangeException();
            return allNums.IndexOf(ch);

        }

        public static double Convert(string p_num, int p, double weight)
        {
            return 0d;
        }
    }
}
