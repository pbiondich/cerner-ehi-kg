# PFT_RULE_ACTION

> This table contains detailed information for each action

**Description:** PFT RULE ACTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DESC` | VARCHAR(200) |  |  | Description of the action. |
| 2 | `ACTION_FIELD` | VARCHAR(200) | NOT NULL |  | Field on which the action is to be performed. |
| 3 | `ACTION_NAME` | VARCHAR(50) | NOT NULL |  | Name of the action. |
| 4 | `ACTION_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Sub-type of the action (i.e. Replace, Append, Prepend, etc.). |
| 5 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Type of action (i.e. Set Value). |
| 6 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 9 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `CREATE_DT_TM` | DATETIME |  |  | The date that the record was created in the table. |
| 12 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for inserting this row on the table |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority of the action. |
| 15 | `RULE_ACTION_ID` | DOUBLE | NOT NULL |  | Unique ID for the action. |
| 16 | `RULE_ID` | DOUBLE | NOT NULL | FK→ | Rule ID of the rule to which the action belongs. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VALUE_DISP` | VARCHAR(200) |  |  | Constant value to be used in Set Value action. |
| 23 | `VALUE_FIELD_NAME` | VARCHAR(200) |  |  | Name of field to be used in Set Value action. |
| 24 | `VALUE_FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | For code values, indicates which part of the code value is to be used. For dates, indicates what format should be used. |
| 25 | `VALUE_FUNCTION_CD` | DOUBLE | NOT NULL |  | Function to be used in the Set Value action. |
| 26 | `VALUE_FUNCTION_PARM` | VARCHAR(100) |  |  | Parameter to be used with function in Set Value action. |
| 27 | `VALUE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Query to be used in Set Value action. |
| 28 | `VALUE_TABLE_CD` | DOUBLE | NOT NULL |  | Table to be used in Set Value action. |
| 29 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Type of value to be used |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RULE_ID` | [PFT_RULE](PFT_RULE.md) | `RULE_ID` |
| `VALUE_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

