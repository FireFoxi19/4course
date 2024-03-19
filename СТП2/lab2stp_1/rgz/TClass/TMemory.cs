using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public class TMemory<T> where T : ANumber, new()
    {
        public enum Commands {
            Store, Add, Clear, Copy
        }

        T number;
        bool state;
        public T FNumber
        {
            get
            {
                state = true;
                return number;
            }
            set
            {
                number = value;
                state = true;
            }
        }
        public bool FState
        {
            get
            {
                return state;
            }

            set
            {
                state = value;
            }
        }

        public TMemory()
        {
            number = new T();
            state = false;
        }

        public TMemory(T num)
        {
            number = num;
            state = false;
        }

        public T Add(T num)
        {
            state = true;
            dynamic a = number;
            dynamic b = num;
            number = a.Add(b);
            return number;
        }

        public void Clear()
        {
            number = new T();
            state = false;
        }

        public (T, bool) Edit(Commands command, T newNumber) {
            switch (command) {
                case Commands.Store:
                    state = true;
                    number = newNumber;
                    break;
                case Commands.Add:
                    dynamic a = number;
                    dynamic b = newNumber;
                    number = a.Add(b);
                    break;
                case Commands.Clear:
                    Clear();
                    break;
            }
            return (number, state);
        }
    }
}
