using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public abstract class AEditor
    {
        public enum Command
        {
            cZero, cOne, cTwo, cThree, cFour, cFive, cSix, cSeven, cEight, cNine,
            cA, cB, cC, cD, cE, cF,
            cSign, cSeparator, cNumbSeparator,
            cBS, cCE, 
            cToggleComplexMode,
            cNone
        }
        public abstract string Number
        {
            get;
            set;
        }
        public abstract string AddNumber(int num);
        public abstract string ToggleMinus();
        public abstract string AddSeparator();
        public abstract string AddZero();
        public abstract bool IsZero();
        public abstract string RemoveSymbol();
        public abstract string Clear();
        public abstract string Edit(Command command);
    }
}
