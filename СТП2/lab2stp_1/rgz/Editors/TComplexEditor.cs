using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace calculator
{
    public class TComplexEditor : AEditor
    {
        public enum PartToEdit
        {
            Real, Imag
        };

        string complex_num;
        PartToEdit mode;
        Regex ZeroComplex = new Regex(@"^-?(0+.?0*)(\s*\+\s*i\s*\*\s*-?(0+.?0*)|(\s*\+\s*i\s*\*\s*-?))?$");
        const string Separator = " + i * ";


        public override string Number
        {
            get
            {
                return complex_num;
            }

            set
            {
                complex_num = new TComplex(value).ToString();
            }
        }

        public TComplexEditor()
        {
            complex_num = "0";
            mode = PartToEdit.Real;
        }

        public TComplexEditor(int a, int b)
        {
            complex_num = new TComplex(a, b).ToString();
            mode = PartToEdit.Real;
        }
        public TComplexEditor(string str)
        {
            complex_num = new TComplex(str).ToString();
            mode = PartToEdit.Real;
        }
        public override bool IsZero()
        {
            return ZeroComplex.IsMatch(complex_num);
        }

        public override string ToggleMinus()
        {
            if (complex_num.Contains(Separator))
            {
                if (mode == PartToEdit.Real)
                {
                    if (complex_num[0] == '-')
                        complex_num = complex_num.Substring(1);
                    else
                        complex_num = '-' + complex_num;
                }
                else
                {
                    complex_num = complex_num.Substring(0, complex_num.IndexOf(Separator)) + Separator + "-" +
                           complex_num.Substring(complex_num.IndexOf(Separator) + Separator.Length);
                }
                return complex_num;
            }
            if (mode == PartToEdit.Imag)
                ToggleMode();
            if (complex_num[0] == '-')
                complex_num = complex_num.Substring(1);
            else
                complex_num = '-' + complex_num;

            return complex_num;
        }

        public PartToEdit ToggleMode()
        {
            if (mode == PartToEdit.Real)
                mode = PartToEdit.Imag;
            else
                mode = PartToEdit.Real;
            return mode;
        }

        public override string AddNumber(int a)
        {
            if (a < 0 || a > 9)
                return complex_num;
            if (a == 0)
                AddZero();
            string left = "", right = "";
            if (complex_num.Contains(Separator))
            {
                left = complex_num.Substring(0, complex_num.IndexOf(Separator));
                right = complex_num.Substring(complex_num.IndexOf(Separator) + +Separator.Length);
            }
            else
            {
                left = complex_num;
            }

            if (mode == PartToEdit.Real)
            {
                if (left == "0" || left == "-0")
                    left = left.First() == '-' ? "-" + a.ToString() : a.ToString();
                else left += a.ToString();
            }
            else
            {
                if (right == "0" || right == "-0")
                    right = right.First() == '-' ? "-" + a.ToString() : a.ToString();
                else right += a.ToString();
            }

            if (right == "")
                complex_num = left;
            else
                complex_num = left + Separator + right;
            return complex_num;
        }

        public override string AddZero()
        {
            if (complex_num == "0" || complex_num == "-0" || complex_num.EndsWith(" 0") || complex_num.EndsWith(" -0") || complex_num.EndsWith(Separator))
                return complex_num;
            complex_num += "0";
            return complex_num;
        }

        public string AddNumberSeparator()
        {
            string left = "", right = "";
            if (complex_num.Contains(Separator))
            {
                left = complex_num.Substring(0, complex_num.IndexOf(Separator));
                right = complex_num.Substring(complex_num.IndexOf(Separator) + Separator.Length);
            }
            else
            {
                left = complex_num;
            }

            if (mode == PartToEdit.Real)
            {
                if (!left.Contains("."))
                    left += ".";
            }
            else
            {
                if (!right.Contains(".") && right.Length > 0)
                    right += ".";
            }

            if (right == "")
                complex_num = left;
            else
                complex_num = left + Separator + right;

            return complex_num;
        }

        public override string AddSeparator()
        {
            if (!complex_num.Contains(Separator))
            {
                complex_num = complex_num + Separator + "0";
                mode = PartToEdit.Imag;
            }
            return complex_num;
        }

        public override string RemoveSymbol()
        {
            string left = "", right = "";
            if (complex_num.Contains(Separator))
            {
                left = complex_num.Substring(0, complex_num.IndexOf(Separator));
                right = complex_num.Substring(complex_num.IndexOf(Separator) + Separator.Length);
            }
            else
            {
                left = complex_num;
            }

            if (mode == PartToEdit.Real)
            {
                if (left.Length == 1 || (left.Length == 2 && left[0] == '-'))
                {
                    left = left[0] == '-' ? "-0" : "0";
                }
                else
                {
                    left = left.Remove(left.Length - 1);
                }
            }
            else
            {
                if (right.Length == 1 || (right.Length == 2 && right[0] == '-'))
                {
                    right = right[0] == '-' ? "-0" : "0";
                }
                else
                {
                    right = right.Remove(right.Length - 1);
                }
            }

            if (right == "")
                complex_num = left;
            else
                complex_num = left + Separator + right;

            return complex_num;
        }

        public override string Clear()
        {
            complex_num = "0";
            mode = PartToEdit.Real;
            return complex_num;
        }

        public override string ToString()
        {
            return complex_num;
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
                    AddNumberSeparator();
                    break;
                case Command.cBS:
                    RemoveSymbol();
                    break;
                case Command.cCE:
                    Clear();
                    break;
                case Command.cNumbSeparator:
                    AddSeparator();
                    break;
                case Command.cToggleComplexMode:
                    ToggleMode();
                    break;
                default:
                    break;
            }
            return complex_num;
        }
    }
}
