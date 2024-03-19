using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public class THistory
    {
        public struct Record
        {
            private string oper;
            private string str_res;
            public Record(string operation, string str_res)
            {
                str_res = str_res.Remove(0, 1);
                this.oper = operation;
                this.str_res = str_res;
            }
            public List<string> ToList()
            {
                return new List<string> { oper, str_res };
            }
        }

        List<Record> L;
        public THistory()
        {
            L = new List<Record>();
        }

        public void AddRecord(string o, string record_string)
        {
            Record record = new Record(o, record_string);
            L.Add(record);
        }

        public Record this[int i]
        {
            get
            {
                if (i < 0 || i >= L.Count)
                    throw new IndexOutOfRangeException();
                return L[i];
            }
            set
            {
                if (i < 0 || i >= L.Count)
                    throw new IndexOutOfRangeException();
                L[i] = value;
            }
        }

        public void Clear()
        {
            L.Clear();
        }

        public int Count()
        {
            return L.Count();
        }
    }
}
