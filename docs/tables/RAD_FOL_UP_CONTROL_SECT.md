# RAD_FOL_UP_CONTROL_SECT

> Stores the general settings for patient follow-up that are section specific.

**Description:** RadNet Follow Up Control by Section  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADVANCE_PRINT_DAYS` | DOUBLE |  |  | The number of days in advance that the follow-up letter should be sent. |
| 2 | `ASSESS_3_DFLT_INTERVAL_MONTHS` | DOUBLE |  |  | Stores the default recall interval in months for studies with Assessment 3. A value of -1 indicates "Now". |
| 3 | `ASSESS_4_DFLT_INTERVAL_MONTHS` | DOUBLE |  |  | Stores the default recall interval in months for studies with Assessment 4. A value of -1 indicates "Now". |
| 4 | `ASSESS_5_DFLT_INTERVAL_MONTHS` | DOUBLE |  |  | Stores the default recall interval in months for studies with Assessment 5. A value of -1 indicates "Now". |
| 5 | `ASSESS_6_DFLT_INTERVAL_MONTHS` | DOUBLE |  |  | Stores the default recall interval in months for studies with Assessment 6. A value of -1 indicates "Now". |
| 6 | `BREAST_DENSITY_STMT_IND` | DOUBLE |  |  | This column will save the responses to "Require breast density statement selection before signing the report" question in follow-up tools. Responses are saved at section level. Possible response values are Yes / No / empty string which is also the default response selected for this question.Planning to store these values as 2 (Yes), 1 (No), 0 (empty string) |
| 7 | `INITIAL_WARNING_DAYS` | DOUBLE |  |  | Number of days after recall date at which to send an OVERDUE warning. |
| 8 | `MAX_WARNING_LETTER_PRINT_NBR` | DOUBLE |  |  | The maximum number of times that a patient or physician warning letter will be printed. |
| 9 | `RAD_FOL_UP_CONTROL_SECT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RAD_FOL_UP_CONTROL_SECT table. |
| 10 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Location for which this follow up control section has been customized. |
| 11 | `SURVEY_ELAPSED_DAYS` | DOUBLE |  |  | The number of days after the study date that the physician survey letter would qualify to print. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `WARNING_INTERVAL_DAYS` | DOUBLE |  |  | If repeated warnings are sent, the number of days between warnings. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

