using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace calculator
{
    public class TPNumberEditor : AEditor
    {
        private string pNumber;

        public int Notation;
        public int Precision;

        Regex ZeroPNumber = new Regex("^-?(0+|.?0+|0+.(0+)?)$");
        const string Separator = ".";

        public override string Number
        {
            get
            {
                return pNumber;
            }

            set
            {
                pNumber = new TPNumber(value, Notation, Precision).ToString();
            }
        }
        public TPNumberEditor()
        {
            pNumber = "0";
            Notation = 10;
            Precision = 5;
        }

        public TPNumberEditor(double num, int not, int pre)
        {
            if (not < 2 || not > 16 || pre < 0 || pre > 10)
            {
                pNumber = "0";
                Notation = 10;
                Precision = 5;
            }
            else
            {
                Notation = not;
                Precision = pre;
                pNumber = TPNumber.ADT_Convert_10_p.Do(num, not, pre);
            }
        }

        public override bool IsZero()
        {
            return ZeroPNumber.IsMatch(pNumber);
        }
        public override string ToggleMinus()
        {
            if (pNumber.ElementAt(0) == '-')
                pNumber = pNumber.Remove(0, 1);
            else
                pNumber = "-" + pNumber;
            return pNumber;
        }

        public override string AddNumber(int num)
        {
            if (num < 0 || num >= Notation)
                return pNumber;
            if (num == 0)
                AddZero();
            else if (pNumber == "0" || pNumber == "-0")
                pNumber = pNumber.First() == '-' ? "-" + TPNumber.ADT_Convert_10_p.Int_to_char(num).ToString() : TPNumber.ADT_Convert_10_p.Int_to_char(num).ToString();
            else
                pNumber += TPNumber.ADT_Convert_10_p.Int_to_char(num).ToString();
            return pNumber;
        }

        public override string RemoveSymbol()
        {
            if (pNumber.Length == 1)
                pNumber = "0";
            else if (pNumber.Length == 2 && pNumber.First() == '-')
                pNumber = "-0";
            else
                pNumber = pNumber.Remove(pNumber.Length - 1);
            return pNumber;
        }
        
        public override string AddSeparator()
        {
            if (!pNumber.Contains(Separator))
                pNumber += Separator;
            return pNumber;
        }

        public override string AddZero()
        {
            if (pNumber.Contains(Separator) && pNumber.Last().ToString() == Separator)
                return pNumber;
            if (pNumber == "0" || pNumber == "0.")
                return pNumber;
            pNumber += "0";
            return pNumber;
        }
        public override string ToString()
        {
            return pNumber;
        }
        public override string Clear()
        {
            pNumber = "0";
            return pNumber;
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
                case Command.cA:
                    AddNumber(10);
                    break;
                case Command.cB:
                    AddNumber(11);
                    break;
                case Command.cC:
                    AddNumber(12);
                    break;
                case Command.cD:
                    AddNumber(13);
                    break;
                case Command.cE:
                    AddNumber(14);
                    break;
                case Command.cF:
                    AddNumber(15);
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
            return Number;
        }
    }
}
