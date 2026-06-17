# AP_PROMPT_TEST

> This activity table contains prompt test information associated with a pathology case. Prompt test information is automatically moved to the appropriate pathology report when the report is modified via an AP result entry application.

**Description:** AP Prompt Test  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to identify the accession value to which order is associated with. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the result information associated withthe prompt text. This internal, system-assigned number could be used to join to the result information stored on the LONG_TEXT table. |
| 4 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the discrete task that represents the prompt test. This value could be used to join to task-specific information stored on the DISCRETE_TASK_ASSAY table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

