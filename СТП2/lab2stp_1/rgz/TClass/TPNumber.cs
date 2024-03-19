using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public class TPNumber : ANumber
    {
        public class ADT_Convert_10_p
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

                string leftSideString = Int_to_p(leftSide, p);
                string rightSideString = Flt_to_p(rightSide, p, c);

                return leftSideString + (rightSideString == String.Empty ? "" : ".") + rightSideString;
            }

            public static char Int_to_char(int d)
            {
                if (d > 15 || d < 0)
                {
                    throw new IndexOutOfRangeException();
                }
                string allSymbols = "0123456789ABCDEF";
                return allSymbols.ElementAt(d);
            }

            public static string Int_to_p(long n, int p)
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
                    buf += Int_to_char((int)n % p);
                    n /= p;
                }

                if (isNegative)
                    buf += "-";

                char[] chs = buf.ToCharArray();
                Array.Reverse(chs);
                return new string(chs);
            }

            public static string Flt_to_p(double n, int p, int c)
            {
                if (p < 2 || p > 16)
                    throw new IndexOutOfRangeException();
                if (c < 0 || c > 10)
                    throw new IndexOutOfRangeException();

                string pNumber = String.Empty;
                for (int i = 0; i < c; i++)
                {
                    pNumber += Int_to_char((int)(n * p));
                    n = n * p - (int)(n * p);
                }
                pNumber = pNumber.TrimEnd('0');
                return pNumber;
            }
        }

        public class ADT_Convert_p_10
        {
            public static double Dval(string p_num, int p)
            {
                if (p < 2 || p > 16)
                    throw new IndexOutOfRangeException();

                bool minus = false;
                if (p_num.Contains("-"))
                {
                    minus = true;
                    p_num = p_num.Replace("-", "");
                }
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
                if (minus)
                {
                    buf = buf * -1;
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

        public double Number;
        public int Notation;
        public int Precision;

        public TPNumber()
        {
            Number = 0f;
            Notation = 10;
            Precision = 5;
        }
        public TPNumber(double num, int not, int pre)
        {
            if (not < 2 || not > 16 || pre < 0 || pre > 10)
            {
                Number = 0f;
                Notation = 10;
                Precision = 5;
            }
            else
            {
                Number = num;
                Notation = not;
                Precision = pre;
            }
        }
        public TPNumber(TPNumber anotherTPNumber)
        {
            Number = anotherTPNumber.Number;
            Notation = anotherTPNumber.Notation;
            Precision = anotherTPNumber.Precision;
        }
        public TPNumber(string str, int not, int pre)
        {
            try
            {
                Number = ADT_Convert_p_10.Dval(str, not);
                Notation = not;
                Precision = pre;
            }
            catch
            {
                throw new System.OverflowException();
            }
        }

        public TPNumber Add(TPNumber a)
        {
            TPNumber tmp = a.Copy();
            if (a.Notation != this.Notation || a.Precision != Precision)
            {
                tmp.Number = 0.0;
                return tmp;
            }
            tmp.Number = Number + a.Number;
            return tmp;
        }

        public TPNumber Mul(TPNumber a)
        {
            TPNumber tmp = a.Copy();
            if (a.Notation != this.Notation || a.Precision != this.Precision)
            {
                tmp.Number = 0.0;
                return tmp;
            }
            tmp.Number = Number * a.Number;
            return tmp;
        }

        public TPNumber Div(TPNumber a)
        {
            TPNumber tmp = a.Copy();
            if (a.Notation != Notation || a.Precision != Precision)
            {
                tmp.Number = 0.0;
                return tmp;
            }
            tmp.Number = Number / a.Number;
            return tmp;
        }
        
        public TPNumber Sub(TPNumber a)
        {
            TPNumber tmp = a.Copy();
            if (a.Notation != Notation || a.Precision != Precision)
            {
                tmp.Number = 0.0;
                return tmp;
            }
            tmp.Number = Number - a.Number;
            return tmp;
        }
        public object Square()
        {
            return new TPNumber(Number * Number, Notation, Precision);
        }
        public object Reverse()
        {
            return new TPNumber(1 / Number, Notation, Precision);
        }
        public bool IsZero()
        {
            return Number == 0;
        }

        public TPNumber Copy()
        {
            return (TPNumber)this.MemberwiseClone();
        }

        public override string ToString()
        {
            string str;
            try
            {
                str = ADT_Convert_10_p.Do(Number, Notation, Precision);

            }
            catch
            {
                throw new System.OverflowException();
            }
            return str;
        }

        public override void SetString(string str)
        {
            try
            {
                Number = ADT_Convert_p_10.Dval(str, Notation);
            }
            catch
            {
                throw new System.OverflowException();
            }
}

        private bool check(double a, int b, int c)
        {
            string a_str = a.ToString();
            if (!checkOnBase(a_str, b))
            {
                return false;
            }
            if (!checkOnC(a_str, c))
            {
                return false;
            }
            if (!checkOnSymbol(a_str))
            {
                return false;
            }
            return true;
        }
        private bool check(string a, string b, string c)
        {
            int b_int = Convert.ToInt32(b);
            int c_int = Convert.ToInt32(c);
            if (!checkOnBase(a, b_int))
            {
                return false;
            }
            if (!checkOnC(a, c_int))
            {
                return false;
            }
            if (!checkOnSymbol(a))
            {
                return false;
            }
            return true;
        }

        private bool checkOnBase(string a, int b)
        {
            foreach (char iter in a)
            {
                int move = Math.Abs('A' - iter);
                int iter_int = iter - '0';
                if (iter >= 'A' && iter <= 'Z')
                {
                    iter_int = 10 + move;
                }
                if (iter == ',')
                {
                    continue;
                }
                if (iter_int >= b)
                {
                    return false;
                }
            }
            return true;
        }

        private bool checkOnC(string a, int c)
        {
            if (checkPoint(a) && c > 0)
            {
                string[] spliter = a.Split(',');
                if (spliter[1].Length == c)
                {
                    return true;
                }
            }
            return false;
        }
        private bool checkPoint(string n)
        {
            int i;
            for (i = 0; i < n.Length && n[i] != ','; i++) { }
            if (i < n.Length)
            {
                return true;
            }
            return false;
        }
        private bool checkOnSymbol(string a)
        {
            foreach (char iter in a)
            {
                if (iter >= 'a' && iter <= 'z')
                {
                    return false;
                }
            }
            return true;
        }
    }
}
