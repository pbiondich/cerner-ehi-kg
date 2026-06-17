# PFT_RULE_QUALIFICATION

> This table contains detailed information for each qualification

**Description:** PFT RULE QUALIFICATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONDITIONAL_CD` | DOUBLE | NOT NULL |  | Conditional to be used in qualification (i.e. AND, OR, etc.). |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date that the record was created in the table. |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for inserting this row on the table |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | Group ID of group to which the qualification belongs. |
| 11 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority of the qualification. |
| 12 | `QUALIFICATION_ID` | DOUBLE | NOT NULL |  | Unique ID for the qualification. |
| 13 | `QUALIFIER_CD` | DOUBLE | NOT NULL |  | Qualifier to be used in qualification (i.e. =, <, >, etc.). |
| 14 | `QUAL_FIELD_NAME` | VARCHAR(200) |  |  | Name of field to be used on the left side of qualifier. |
| 15 | `QUAL_FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | For code values, indicates which part of the code value is to be used. For dates, indicates what format should be used. |
| 16 | `QUAL_FUNCTION_CD` | DOUBLE | NOT NULL |  | Function to be used on the left side of the qualifier (i.e. COUNT, SUM, etc.). |
| 17 | `QUAL_FUNCTION_PARM` | VARCHAR(100) |  |  | Parameter to be used with the function on the left side of the qualifier. |
| 18 | `QUAL_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies qualifier field content for XPath. |
| 19 | `QUAL_TABLE_CD` | DOUBLE | NOT NULL |  | Table to be used on the left side of the qualifier. |
| 20 | `QUAL_TYPE_FLAG` | DOUBLE | NOT NULL |  | This column represents the data type of the qualification field, which is the left hand side operand of a qualification rule.2 - Table/Field5 - XPath |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VALUE_DISP` | VARCHAR(200) |  |  | Constant value to be used on the right side of the qualifier. |
| 27 | `VALUE_FIELD_NAME` | VARCHAR(200) |  |  | Name of the field to be used on the left side of the qualifier. |
| 28 | `VALUE_FUNCTION_CD` | DOUBLE | NOT NULL |  | Function to be used on the right side of the qualifier. |
| 29 | `VALUE_FUNCTION_PARM` | VARCHAR(100) |  |  | Parameter to be used with the function on the right side of the qualifier. |
| 30 | `VALUE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Query to be used on the right side of the qualifier. |
| 31 | `VALUE_TABLE_CD` | DOUBLE | NOT NULL |  | Table to be used on the left side of the qualifier. |
| 32 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Type of value to be used on the right side of the qualifier. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `GROUP_ID` | [PFT_RULE_GROUP](PFT_RULE_GROUP.md) | `GROUP_ID` |
| `QUAL_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `VALUE_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

