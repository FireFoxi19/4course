using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace calculator
{
    public partial class Form1 : Form
    {
        ADT_Control<TFrac, TFracEditor> fracController;
        ADT_Control<TComplex, TComplexEditor> complexController;
        ADT_Control<TPNumber, TPNumberEditor> pNumberController;

        const string operation_signs = "+-/*";
        bool fracMode = true;
        bool complexMode = true;
        bool pNumberMode = true;
        string memmory_buffer = string.Empty;


        const string TAG_FRAC = "FRAC_";
        const string TAG_COMPLEX = "COMPLEX_";
        const string TAG_PNUMBER = "PNUMBER_";

        public Form1()
        {
            fracController = new ADT_Control<TFrac, TFracEditor>();
            complexController = new ADT_Control<TComplex, TComplexEditor>();
            pNumberController = new ADT_Control<TPNumber, TPNumberEditor>();
            InitializeComponent();
        }

        private string NumberBeautifier(string Tag, string v)
        {
            if (v == "ERROR")
                return v;
            string toReturn = v;
            if (fracMode == true)
                toReturn = v;
            else if (new TFrac(v).getDenominatorNum() == 1)
                toReturn = new TFrac(v).getNumeratorString();

            switch (Tag)
            {
                case TAG_PNUMBER:
                    break;
                case TAG_FRAC:
                    if (fracMode == true)
                        toReturn = v;
                    else if (new TFrac(v).Denominator == 1)
                        toReturn = new TFrac(v).Numerator.ToString();
                    break;
                case TAG_COMPLEX:
                    if (complexMode == true)
                        toReturn = v;
                    else if (new TComplex(v).Imaginary == 0)
                        toReturn = new TComplex(v).Real.ToString();
                    break;
            }

            return toReturn;
        }

        private void CopyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            memmory_buffer = tB_Frac.Text;

        }

        private void EnterToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (memmory_buffer == string.Empty)
            {
                MessageBox.Show("Буфер обмена пуст.\n" +
                    "Нечего вставить.",
                    "Ошибка",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation);
                return;
            }
            foreach (char i in memmory_buffer)
                tB_Frac.Text = fracController.ExecCommandEditor(CharToEditorCommand(i));
        }

        private static AEditor.Command CharToEditorCommand(char ch)
        {
            AEditor.Command command = AEditor.Command.cNone;
            switch (ch)
            {
                case '0':
                    command = AEditor.Command.cZero;
                    break;
                case '1':
                    command = AEditor.Command.cOne;
                    break;
                case '2':
                    command = AEditor.Command.cTwo;
                    break;
                case '3':
                    command = AEditor.Command.cThree;
                    break;
                case '4':
                    command = AEditor.Command.cFour;
                    break;
                case '5':
                    command = AEditor.Command.cFive;
                    break;
                case '6':
                    command = AEditor.Command.cSix;
                    break;
                case '7':
                    command = AEditor.Command.cSeven;
                    break;
                case '8':
                    command = AEditor.Command.cEight;
                    break;
                case '9':
                    command = AEditor.Command.cNine;
                    break;
                case 'A':
                    command = AEditor.Command.cA;
                    break;
                case 'B':
                    command = AEditor.Command.cB;
                    break;
                case 'C':
                    command = AEditor.Command.cC;
                    break;
                case 'D':
                    command = AEditor.Command.cD;
                    break;
                case 'E':
                    command = AEditor.Command.cE;
                    break;
                case 'F':
                    command = AEditor.Command.cF;
                    break;
                case '.':
                    command = AEditor.Command.cSeparator;
                    break;
                case '-':
                    command = AEditor.Command.cSign;
                    break;
                case 'i':
                    command = AEditor.Command.cToggleComplexMode;
                    break;
            }

            return command;
        }
        private static ADT_Proc<T>.Operations CharToOperationsCommand<T>(char ch) where T : ANumber, new()
        {
            ADT_Proc<T>.Operations command = ADT_Proc<T>.Operations.None;
            switch (ch)
            {
                case '+':
                    command = ADT_Proc<T>.Operations.Add;
                    break;
                case '-':
                    command = ADT_Proc<T>.Operations.Sub;
                    break;
                case '*':
                    command = ADT_Proc<T>.Operations.Mul;
                    break;
                case '/':
                    command = ADT_Proc<T>.Operations.Div;
                    break;
            }

            return command;
        }

        private static AEditor.Command KeyCodeToEditorCommand(Keys ch)
        {
            AEditor.Command command = AEditor.Command.cNone;
            switch (ch)
            {
                case Keys.Back:
                    command = AEditor.Command.cBS;
                    break;
                case Keys.Delete:
                case Keys.Escape:
                    command = AEditor.Command.cCE;
                    break;
            }

            return command;
        }


        private void AboutToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("группа: ИП-013 ~~Копытина Татьяна~~    ~~Семилетко Максим~~", "Справка", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void Button_Number_Edit(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            string Tag = button.Tag.ToString();
            
            if (Tag.StartsWith(TAG_FRAC))
            {
                string tag_command = Tag.Replace(TAG_FRAC, string.Empty);
                Enum.TryParse(tag_command, out AEditor.Command ParsedEnum);
                tB_Frac.Text = fracController.ExecCommandEditor(ParsedEnum);
            }
            else if (Tag.StartsWith(TAG_COMPLEX))
            {
                string tag_command = Tag.Replace(TAG_COMPLEX, string.Empty);
                Enum.TryParse(tag_command, out AEditor.Command ParsedEnum);
                tB_Complex.Text = complexController.ExecCommandEditor(ParsedEnum);
            }
            else if (Tag.StartsWith(TAG_PNUMBER))
            {
                string tag_command = Tag.Replace(TAG_PNUMBER, string.Empty);
                Enum.TryParse(tag_command, out AEditor.Command ParsedEnum);
                tB_PNumber.Text = pNumberController.ExecCommandEditor(ParsedEnum);
            }

        }

        private void Button_Number_Operation(object sender, EventArgs e)
        {

            Button button = (Button)sender;
            string Tag = button.Tag.ToString();

            if (Tag.StartsWith(TAG_FRAC))
            {
                string tag_command = Tag.Replace(TAG_FRAC, string.Empty);
                Enum.TryParse(tag_command, out ADT_Proc<TFrac>.Operations ParsedEnum);
                tB_Frac.Text = NumberBeautifier(TAG_FRAC, fracController.ExecOperation(ParsedEnum));
            }
            else if (Tag.StartsWith(TAG_COMPLEX))
            {
                string tag_command = Tag.Replace(TAG_COMPLEX, string.Empty);
                Enum.TryParse(tag_command, out ADT_Proc<TComplex>.Operations ParsedEnum);
                tB_Complex.Text = NumberBeautifier(TAG_COMPLEX, complexController.ExecOperation(ParsedEnum));
            }
            else if (Tag.StartsWith(TAG_PNUMBER))
            {
                string tag_command = Tag.Replace(TAG_PNUMBER, string.Empty);
                Enum.TryParse(tag_command, out ADT_Proc<TPNumber>.Operations ParsedEnum);
                tB_PNumber.Text = NumberBeautifier(TAG_PNUMBER, pNumberController.ExecOperation(ParsedEnum));
            }
        }

        private void Button_Number_Function(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            string Tag = button.Tag.ToString();

            if (Tag.StartsWith(TAG_FRAC))
            {
                string tag_command = Tag.Replace(TAG_FRAC, string.Empty);
                Enum.TryParse(tag_command, out ADT_Proc<TFrac>.Functions ParsedEnum);
                tB_Frac.Text = NumberBeautifier(TAG_FRAC, fracController.ExecFunction(ParsedEnum));
            }
            else if (Tag.StartsWith(TAG_COMPLEX))
            {
                string tag_command = Tag.Replace(TAG_COMPLEX, string.Empty);
                Enum.TryParse(tag_command, out ADT_Proc<TComplex>.Functions ParsedEnum);
                tB_Complex.Text = NumberBeautifier(TAG_COMPLEX, complexController.ExecFunction(ParsedEnum));
            }
            else if (Tag.StartsWith(TAG_PNUMBER))
            {
                string tag_command = Tag.Replace(TAG_PNUMBER, string.Empty);
                Enum.TryParse(tag_command, out ADT_Proc<TPNumber>.Functions ParsedEnum);
                tB_PNumber.Text = NumberBeautifier(TAG_PNUMBER, pNumberController.ExecFunction(ParsedEnum));
            }
        }

        private void Button_Memory(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            string Tag = button.Tag.ToString();
            if (Tag.StartsWith(TAG_FRAC))
            {
                string tag_command = Tag.Replace(TAG_FRAC, string.Empty);
                Enum.TryParse(tag_command, out TMemory<TFrac>.Commands ParsedEnum);
                dynamic exec = fracController.ExecCommandMemory(ParsedEnum, tB_Frac.Text);
                if (ParsedEnum == TMemory<TFrac>.Commands.Copy)
                    tB_Frac.Text = exec.Item1.ToString();
                label_Frac_Memory.Text = exec.Item2 == true ? "M" : string.Empty;
            }
            else if (Tag.StartsWith(TAG_COMPLEX))
            {
                string tag_command = Tag.Replace(TAG_COMPLEX, string.Empty);
                Enum.TryParse(tag_command, out TMemory<TComplex>.Commands ParsedEnum);
                dynamic exec = complexController.ExecCommandMemory(ParsedEnum, tB_Complex.Text);
                if (ParsedEnum == TMemory<TComplex>.Commands.Copy)
                    tB_Complex.Text = exec.Item1.ToString();
                label_Complex_Memory.Text = exec.Item2 == true ? "M" : string.Empty;
            }
            else if (Tag.StartsWith(TAG_PNUMBER))
            {
                string tag_command = Tag.Replace(TAG_PNUMBER, string.Empty);
                Enum.TryParse(tag_command, out TMemory<TPNumber>.Commands ParsedEnum);
                dynamic exec = pNumberController.ExecCommandMemory(ParsedEnum, tB_Complex.Text);
                if (ParsedEnum == TMemory<TPNumber>.Commands.Copy)
                    tB_PNumber.Text = exec.Item1.ToString();
                label_PNumber_Memory.Text = exec.Item2 == true ? "M" : string.Empty;
            }
        }

        private void Button_Reset(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            string Tag = button.Tag.ToString();
            if (Tag.StartsWith(TAG_FRAC))
            {
                tB_Frac.Text = fracController.Reset();
                label_Frac_Memory.Text = string.Empty;
            }
            else if (Tag.StartsWith(TAG_COMPLEX))
            {
                tB_Complex.Text = complexController.Reset();
                label_Complex_Memory.Text = string.Empty;
            }
            else if (Tag.StartsWith(TAG_PNUMBER))
            {
                tB_PNumber.Text = pNumberController.Reset();
                label_PNumber_Memory.Text = string.Empty;
            }

        }

        private void Button_Calculate(object sender, EventArgs e)
        {
            Button button = (Button)sender;
            string Tag = button.Tag.ToString();
            if (Tag.StartsWith(TAG_FRAC))
            {
                tB_Frac.Text = NumberBeautifier(TAG_FRAC, fracController.Calculate());
            }
            else if (Tag.StartsWith(TAG_COMPLEX))
            {
                tB_Complex.Text = NumberBeautifier(TAG_COMPLEX, complexController.Calculate());
            }
            else if (Tag.StartsWith(TAG_PNUMBER))
            {
                tB_PNumber.Text = pNumberController.Calculate();
            }
        }

        private void TrackBar_PNumber_ValueChanged(object sender, EventArgs e)
        {
            label_PNumber_P.Text = trackBar_PNumber.Value.ToString();
            pNumberController.Edit.Notation = trackBar_PNumber.Value;
            tB_PNumber.Text = pNumberController.Reset();
            label_PNumber_Memory.Text = string.Empty;
            string AllowedEndings = "0123456789ABCDEF";
            foreach (Control i in tabPage_PNumber.Controls.OfType<Button>())
            {
                if (AllowedEndings.Contains(i.Name.ToString().Last()) && i.Name.ToString().Substring(i.Name.ToString().Length - 2, 1) == "_")
                {
                    int j = AllowedEndings.IndexOf(i.Name.ToString().Last());
                    if (j < trackBar_PNumber.Value)
                    {
                        i.Enabled = true;
                    }
                    if ((j >= trackBar_PNumber.Value) && (j <= 15))
                    {
                        i.Enabled = false;
                    }
                }
            }
            pNumberController.Proc.Left_Result_operand.Notation = trackBar_PNumber.Value;
            pNumberController.Proc.Right_operand.Notation = trackBar_PNumber.Value;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            

            switch (tabControl.SelectedIndex)
            {
                case 0: {
                    if (e.KeyCode == Keys.Enter)
                        b_Frac_Eval.PerformClick();
                    else
                    {
                        AEditor.Command command = KeyCodeToEditorCommand(e.KeyCode);
                        if (command != AEditor.Command.cNone)
                            tB_Frac.Text = fracController.ExecCommandEditor(command);
                    }
                    break;
                }
                case 1: {
                    if (e.KeyCode == Keys.Enter)
                        b_Complex_Eval.PerformClick();
                    else
                    {
                        AEditor.Command command = KeyCodeToEditorCommand(e.KeyCode);
                        if (command != AEditor.Command.cNone)
                            tB_Complex.Text = complexController.ExecCommandEditor(command);
                    }
                    break;
                }
                case 2: {
                    if (e.KeyCode == Keys.Enter)
                        b_Complex_Eval.PerformClick();
                    else
                    {
                        AEditor.Command command = KeyCodeToEditorCommand(e.KeyCode);
                        if (command != AEditor.Command.cNone)
                            tB_Complex.Text = pNumberController.ExecCommandEditor(command);
                    }
                    break;
                }
                default:
                    break;
            }
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            switch (tabControl.SelectedIndex)
            {
                case 0: {
                    if (e.KeyChar >= '0' && e.KeyChar <= '9' || e.KeyChar == '.')
                        tB_Frac.Text = fracController.ExecCommandEditor(CharToEditorCommand(e.KeyChar));
                    else if (operation_signs.Contains(e.KeyChar))
                        tB_Frac.Text = NumberBeautifier(TAG_FRAC, fracController.ExecOperation(CharToOperationsCommand<TFrac>(e.KeyChar)));
                    break;
                }
                case 1: {
                    if ((e.KeyChar >= '0' && e.KeyChar <= '9') || e.KeyChar == '.')
                        tB_Complex.Text = complexController.ExecCommandEditor(CharToEditorCommand(e.KeyChar));
                    else if (operation_signs.Contains(e.KeyChar))
                        tB_Complex.Text = NumberBeautifier(TAG_COMPLEX, complexController.ExecOperation(CharToOperationsCommand<TComplex>(e.KeyChar)));
                    break;
                }
                case 2: {
                    if ((e.KeyChar >= '0' && e.KeyChar <= '9') || (e.KeyChar >= 'A' && e.KeyChar <= 'F') || (e.KeyChar == '.'))
                        tB_PNumber.Text = pNumberController.ExecCommandEditor(CharToEditorCommand(e.KeyChar));
                    else if (operation_signs.Contains(e.KeyChar))
                        tB_PNumber.Text = NumberBeautifier(TAG_PNUMBER, pNumberController.ExecOperation(CharToOperationsCommand<TPNumber>(e.KeyChar)));
                    break;
                }
                default:
                    break;
            }
        }
        private void HistoryToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Form2 history = new Form2();
            history.Show();
            if (fracController.history.Count() == 0)
            {
                MessageBox.Show("История пуста", "Внимание", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            for (int i = 0; i < fracController.history.Count(); i++)
            {
                List<string> currentRecord = fracController.history[i].ToList();
                history.dataGridView1.Rows.Add(currentRecord[0], currentRecord[1]);
            }
            for (int i = 0; i < complexController.history.Count(); i++)
            {
                List<string> currentRecord = complexController.history[i].ToList();
                history.dataGridView1.Rows.Add(currentRecord[0], currentRecord[1]);
            }
            for (int i = 0; i < pNumberController.history.Count(); i++)
            {
                List<string> currentRecord = pNumberController.history[i].ToList();
                history.dataGridView1.Rows.Add(currentRecord[0], currentRecord[1]);
            }
        }

        private void дробьFracTSMI_Click(object sender, EventArgs e)
        {
            дробьFracTSMI.Checked = true;
            числоFracTSMI.Checked = false;
            fracMode = true;
        }

        private void числоFracTSMI_Click(object sender, EventArgs e)
        {
            дробьFracTSMI.Checked = false;
            числоFracTSMI.Checked = true;
            fracMode = false;
        }

        private void комплексноеComplexTSMI_Click(object sender, EventArgs e)
        {
            комплексноеComplexTSMI.Checked = true;
            действительноеComplexTSMI.Checked = false;
            complexMode = true;
        }

        private void действительноеComplexTSMI_Click(object sender, EventArgs e)
        {
            комплексноеComplexTSMI.Checked = false;
            действительноеComplexTSMI.Checked = true;
            complexMode = false;
        }

        private void label_Frac_Memory_Click(object sender, EventArgs e)
        {

        }
    }
}
