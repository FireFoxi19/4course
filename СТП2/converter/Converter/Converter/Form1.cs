using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Converter
{
    public partial class Form1 : Form
    {
        Controller control_ = new Controller();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = control_.editor.getNumber();
            trackBar1.Value = control_.Pin;
            trackBar2.Value = control_.Pout;
            label2.Text = "0";
            UpdateButtons();
        }

        private void UpdateButtons()
        {
            foreach (Control i in Controls)
            {
                if (i is Button)
                {
                    int j = Convert.ToInt16(i.Tag.ToString());
                    if (j < trackBar1.Value)
                        i.Enabled = true;
                    if ((j >= trackBar1.Value) && (j <= 15))
                        i.Enabled = false;
                }
            }
        }

        private void trackbar1_Scroll(object sender, EventArgs e)
        {
            numericUpDown1.Value = trackBar1.Value;
            UpdateP1();
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            trackBar1.Value = Convert.ToByte(numericUpDown1.Value);
            UpdateP1();
        }

        private void UpdateP1()
        {
            control_.Pin = trackBar1.Value;
            UpdateButtons();
            label1.Text = control_.doCmnd(18);
            label2.Text = "0";
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            numericUpDown2.Value = trackBar2.Value;
            this.updateP2();
        }
        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            trackBar2.Value = Convert.ToByte(numericUpDown2.Value);
            this.updateP2();
        }
        private void updateP2()
        {
            control_.Pout = trackBar2.Value;
            label2.Text = control_.doCmnd(19);
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void historyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 history = new Form2();
            history.Show();
            if (control_.history.count() == 0)
            {
                MessageBox.Show("История пуста", "Внимание", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            for (int i = 0; i < control_.history.count(); i++)
            {
                List<string> currentRecord = control_.history[i].toList();
                history.dataGridView1.Rows.Add(currentRecord[0], currentRecord[1], currentRecord[2], currentRecord[3]);
            }
        }

        private void infoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("\n" +
                "ИП-013 Копытина, Семилетко.", "Справка", MessageBoxButtons.OK, MessageBoxIcon.Information);

        }

        private void doCmnd(int j)
        {
            if (j == 19)
                label2.Text = control_.doCmnd(j);
            else
            {
                if (control_._State == Controller.State.Converted)
                    label1.Text = control_.doCmnd(18);
                label1.Text = control_.doCmnd(j);
                label2.Text = "0";
            }
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            int i = -1;
            if (e.KeyChar >= 'A' && e.KeyChar <= 'F')
            {
                i = (int)e.KeyChar - 'A' + 10;
            }
            if (e.KeyChar >= '0' && e.KeyChar <= '9')
            {
                i = (int)e.KeyChar - '0';
            }
            if (e.KeyChar == '.')
            {
                i = 16;
            }
            if ((int)e.KeyChar == 8)
            {
                i = 17;
            }
            if ((int)e.KeyChar == 13)
            {
                i = 19;
            }
            if ((i < control_.Pin) || (i >= 16))
            {
                doCmnd(i);
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Delete) {
                doCmnd(18);
            }
            if (e.KeyCode == Keys.Execute) {
                doCmnd(19);
            }
            if (e.KeyCode == Keys.Decimal) {
                doCmnd(16);
            }
        }

        private void button_Click(object sender, EventArgs e)
        {
            Button but = (Button)sender;
            int j = Convert.ToInt16(but.Tag.ToString());
            doCmnd(j);
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
