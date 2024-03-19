using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public class TFracEditor : AEditor
    {
        
        const string Separator = "/";
        const string ZeroFraction = "0/";
        const int max_numerator_length = 14;
        const int max_denominator_length = 22;
        private string fraction;

        public override string Number
        {
            get
            {
                return fraction;
            }

            set
            {
                fraction = new TFrac(value).ToString();
            }
        }

        public TFracEditor()
        {
            fraction = "0";
        }

        public TFracEditor(long a, long b)
        {
            fraction = new TFrac(a, b).ToString();
        }

        public TFracEditor(string frac)
        {
            fraction = new TFrac(frac).ToString();
        }

        public override bool IsZero()
        {
            return fraction.StartsWith(ZeroFraction) || fraction.StartsWith("-" + ZeroFraction) || fraction == "0" || fraction == "-0";
        }

        public override string ToggleMinus()
        {
            if (fraction[0] == '-')
                fraction = fraction.Remove(0, 1);
            else
                fraction = '-' + fraction;

            return fraction;
        }

        public override string AddNumber(int a)
        {
            if (!fraction.Contains(Separator) && fraction.Length > max_numerator_length)
                return fraction;
            else if (fraction.Length > max_denominator_length)
                return fraction;
            if (a < 0 || a > 9)
                return fraction;
            if (a == 0)
                AddZero();
            else if (IsZero())
                fraction = fraction.First() == '-' ? "-" + a.ToString() : a.ToString();
            else
                fraction += a.ToString();

            return fraction;
        }

        public override string AddZero()
        {
            if (IsZero())
                return fraction;
            if (fraction.Last().ToString() == Separator)
                return fraction;
            fraction += "0";

            return fraction;
        }

        public override string RemoveSymbol()
        {
            if (fraction.Length == 1)
                fraction = "0";
            else if (fraction.Length == 2 && fraction.First() == '-')
                fraction = "-0";
            else
                fraction = fraction.Remove(fraction.Length - 1);

            return fraction;
        }

        public override string Clear()
        {
            fraction = "0";

            return fraction;
        }

        public override string Edit(Command command)
        {
            switch (command)
            {
                case Command.cZero:
                    AddZero();
                    break;
                case Command.cOne:
                    AddNumber(1);
                    break;
                case Command.cTwo:
                    AddNumber(2);
                    break;
                case Command.cThree:
                    AddNumber(3);
                    break;
                case Command.cFour:
                    AddNumber(4);
                    break;
                case Command.cFive:
                    AddNumber(5);
                    break;
                case Command.cSix:
                    AddNumber(6);
                    break;
                case Command.cSeven:
                    AddNumber(7);
                    break;
                case Command.cEight:
                    AddNumber(8);
                    break;
                case Command.cNine:
                    AddNumber(9);
                    break;
                case Command.cSign:
                    ToggleMinus();
                    break;
                case Command.cSeparator:
                    AddSeparator();
                    break;
                case Command.cBS:
                    RemoveSymbol();
                    break;
                case Command.cCE:
                    Clear();
                    break;
                default:
                    break;
            }

            return fraction;
        }

        public override string AddSeparator()
        {
            if (!fraction.Contains(Separator))
                fraction += Separator;

            return fraction;
        }

        public override string ToString()
        {
            return Number;
        }
    }
}
