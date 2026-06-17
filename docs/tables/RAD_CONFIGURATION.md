# RAD_CONFIGURATION

> This table contains configuration settings specific to radnet.

**Description:** RadNet Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARAMETER_DESC` | VARCHAR(255) |  |  | The parameter_desc field conations descriptive information about a parameter |
| 2 | `PARAMETER_NAME` | VARCHAR(60) | NOT NULL |  | The parameter_name field names a radiology configuration parameter |
| 3 | `RAD_CONFIGURATION_ID` | DOUBLE | NOT NULL |  | The Rad_Configuration_Id uniquely identifies a row in the Rad_Configuration table. It serves no other purpose other than to uniquely identify the row |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE_DT_TM` | DATETIME |  |  | The value_date field contains date data about a parameter |
| 10 | `VALUE_NUM` | DOUBLE |  |  | The value_num field contains numerical data about a parameter |
| 11 | `VALUE_TEXT` | VARCHAR(255) |  |  | The value_text field contains textual data about a parameter |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

