using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public class ADT_Proc<T> where T : ANumber, new()
    {
        public enum Operations
        {
            None, Add, Sub, Mul, Div
        }
        public enum Functions
        {
            Rev, Sqr
        }

        T left_result_operand;
        T right_operand;
        Operations operation;

        public T Left_Result_operand
        {
            get 
            { 
                return left_result_operand; 
            }

            set 
            {
                left_result_operand = value;
            }
        }
        public T Right_operand
        {
            get
            {
                return right_operand;
            }

            set
            {
                right_operand = value;
            }
        }

        public Operations Operation
        {
            get 
            { 
                return operation; 
            }

            set
            {
                operation = value;
            }
        }

        public ADT_Proc()
        {
            operation = Operations.None;
            left_result_operand = new T();
            right_operand = new T();
        }

        public ADT_Proc(T leftObj, T rightObj)
        {
            operation = Operations.None;
            left_result_operand = leftObj;
            right_operand = rightObj;
        }

        public void ResetProc()
        {
            operation = Operations.None;
            T newObj = new T();
            left_result_operand = right_operand = newObj;
        }

        public void DoOperation()
        {
            try
            {
                dynamic a = left_result_operand;
                dynamic b = right_operand;
                switch (operation)
                {
                    case Operations.Add:
                        left_result_operand = a.Add(b);
                        break;
                    case Operations.Sub:
                        left_result_operand = a.Sub(b);
                        break;
                    case Operations.Mul:
                        left_result_operand = a.Mul(b);
                        break;
                    case Operations.Div:
                        left_result_operand = a.Div(b);
                        break;
                    default:
                        left_result_operand = right_operand;
                        break;
                }
            }
            catch
            {
                throw new System.OverflowException();
            }
        }

        public void DoFunction(Functions function)
        {
            dynamic a = right_operand;
            switch (function)
            {
                case Functions.Rev:
                    a = a.Reverse();
                    right_operand = (T)a;
                    break;
                case Functions.Sqr:
                    a = a.Square();
                    right_operand = (T)a;
                    break;
                default:
                    break;
            }
        }
    }
}
