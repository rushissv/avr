int ind=0;
for(ind=0;ind<20;++ind)
{
  OC1A = pwm_[ind];
  _delyay_ms(2000);
}

for(ind=19;ind>=0;--ind)
{
  OC1A = pwm_[ind];
  _delyay_ms(2000);
}
