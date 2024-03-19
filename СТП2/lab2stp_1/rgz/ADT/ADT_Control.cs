using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    public class ADT_Control<T, TEditor>
        where T : ANumber, new()
        where TEditor : AEditor, new()
    {
        public enum ADT_Control_State { cStart, cEditing, FunDone, cValDone, cExpDone, cOpDone, cOpChange, cError }

        ADT_Control_State calcState;
        TEditor editor;
        ADT_Proc<T> proc;
        TMemory<T> memory;
        public THistory history = new THistory();

        public ADT_Control_State CurState
        {
            get 
            {
                return calcState;
            }
            set
            {
                calcState = value;
            }
        }
        public ADT_Proc<T> Proc
        {
            get
            { 
                return proc; 
            }
            set
            {
                proc = value;
            }
        }

        public TMemory<T> Memory
        {
            get
            { 
                return memory; 
            }
            set
            {
                memory = value;
            }
        }

        public TEditor Edit
        {
            get
            {
                return editor; 
            }
            set
            {
                editor = value;
            }
        }

        public ADT_Control()
        {
            Edit = new TEditor();
            Proc = new ADT_Proc<T>();
            Memory = new TMemory<T>();
            CurState = ADT_Control_State.cStart;
        }

        public string Reset()
        {
            Edit.Clear();
            Proc.ResetProc();
            Memory.Clear();
            CurState = ADT_Control_State.cStart;
            return Edit.ToString();
        }

        public string ExecCommandEditor(AEditor.Command command)
        {
            string toReturn;
            if (CurState == ADT_Control_State.cExpDone)
            {
                Proc.ResetProc();
                CurState = ADT_Control_State.cStart;
            }
            if (CurState != ADT_Control_State.cStart)
                CurState = ADT_Control_State.cEditing;
            toReturn = Edit.Edit(command);
            T tmp = new T();
            if (tmp is TPNumber)
            {
                dynamic a = tmp;
                dynamic b = Edit;
                a.Notation = b.Notation;
                tmp = a;
            }
            tmp.SetString(toReturn);
            proc.Right_operand = tmp;
            history.AddRecord(toReturn, command.ToString());

            return toReturn;
        }

        public string ExecOperation(ADT_Proc<T>.Operations operation)
        {
            if (operation == ADT_Proc<T>.Operations.None)
                return Edit.Number;
            string toReturn;
            try
            {
                switch (CurState)
                {
                    case ADT_Control_State.cStart:
                        Proc.Left_Result_operand = Proc.Right_operand;
                        Proc.Operation = operation;
                        CurState = ADT_Control_State.cOpDone;
                        Edit.Clear();
                        break;
                    case ADT_Control_State.cEditing:
                        Proc.DoOperation();
                        Proc.Operation = operation;
                        Edit.Clear();
                        CurState = ADT_Control_State.cOpDone;
                        break;
                    case ADT_Control_State.FunDone:
                        if (Proc.Operation == 0)
                            Proc.Left_Result_operand = Proc.Right_operand;
                        else
                            Proc.DoOperation();
                        Proc.Operation = operation;
                        Edit.Clear();
                        CurState = ADT_Control_State.cOpChange;
                        Proc.Right_operand = Proc.Left_Result_operand;
                        break;
                    case ADT_Control_State.cOpDone:
                        CurState = ADT_Control_State.cOpChange;
                        Edit.Clear();
                        break;
                    case ADT_Control_State.cValDone:
                        break;
                    case ADT_Control_State.cExpDone:
                        Proc.Operation = operation;
                        Proc.Right_operand = Proc.Left_Result_operand;
                        CurState = ADT_Control_State.cOpChange;
                        Edit.Clear();
                        break;
                    case ADT_Control_State.cOpChange:
                        Proc.Operation = operation;
                        Edit.Clear();
                        break;
                    case ADT_Control_State.cError:
                        Proc.ResetProc();
                        return "ERR";
                }
                toReturn = Proc.Left_Result_operand.ToString();
            }
            catch
            {
                Reset();
                return "ERROR";
            }
            history.AddRecord(toReturn, operation.ToString());

            return toReturn;
        }

        public string ExecFunction(ADT_Proc<T>.Functions function)
        {
            string toReturn;
            try
            {
                if (CurState == ADT_Control_State.cExpDone)
                {
                    Proc.Right_operand = Proc.Left_Result_operand;
                    Proc.Operation = ADT_Proc<T>.Operations.None;
                }
                Proc.DoFunction(function);
                CurState = ADT_Control_State.FunDone;
                toReturn = Proc.Right_operand.ToString();
            }
            catch
            {
                Reset();
                return "ERROR";
            }
            history.AddRecord(toReturn, function.ToString());

            return toReturn;
        }

        public string Calculate()
        {
            string ToReturn;
            try
            {
                if (CurState == ADT_Control_State.cStart)
                    Proc.Left_Result_operand = Proc.Right_operand;
                Proc.DoOperation();
                CurState = ADT_Control_State.cExpDone;
                ToReturn = Proc.Left_Result_operand.ToString();
            }
            catch
            {
                Reset();
                return "ERROR";
            }

            return ToReturn;
        }

        public (T, bool) ExecCommandMemory(TMemory<T>.Commands command, string str)
        {
            T TempObj = new T();
            TempObj.SetString(str);
            (T, bool) obj = (null, false);
            try
            {
                obj = Memory.Edit(command, TempObj);
            }
            catch
            {
                Reset();
                return obj;
            }
            if (command == TMemory<T>.Commands.Copy)
            {
                Edit.Number = obj.Item1.ToString();
                Proc.Right_operand = obj.Item1;
            }
            return obj;
        }
    }
}
