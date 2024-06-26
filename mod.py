import React from 'react';
import { SearchInput } from '@patternfly/react-core';

export const SearchInputWithSubmitButton: React.FunctionComponent = () => {
  const [value, setValue] = React.useState('');

  return (
    <SearchInput
      placeholder="Find by name"
      value={value}
      onChange={(_event, value) => setValue(value)}
      onSearch={(_event, value) => setValue(value)}
      onClear={() => setValue('')}
    />
  );
};


display: flex;
width: 469px;
min-height: 36px;
max-height: 36px;
padding: 6px 8px;
align-items: center;
gap: 4px;


background: var(--Secondary---pf-v5-global--secondary-color--100, #6A6E73);

/* Form/Form toggles default */
box-shadow: 0px -1px 0px 0px #8A8D90 inset, 1px 0px 0px 0px #F0F0F0 inset, 0px 1px 0px 0px #F0F0F0 inset, -1px 0px 0px 0px #F0F0F0 inset;


Secondary/--pf-v5-global--secondary-color--100
Text/--pf-v5-global--Color--light-100
Icon Colors/Dark/--pf-v5-global--icon--Color--dark--light
