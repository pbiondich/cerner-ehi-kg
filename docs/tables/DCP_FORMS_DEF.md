# DCP_FORMS_DEF

> Defines what sections are included in a single form

**Description:** DCP FORMS DEF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DCP_FORMS_DEF_ID` | DOUBLE | NOT NULL |  | unique row identifier |
| 3 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL |  | Identifies the form that the definition is for. |
| 4 | `DCP_FORM_INSTANCE_ID` | DOUBLE | NOT NULL |  | Identifies the form version that the definition is for. |
| 5 | `DCP_SECTION_REF_ID` | DOUBLE | NOT NULL |  | section id of the section that is on the form. |
| 6 | `FLAGS` | DOUBLE |  |  | Bitwise flags to specify defined behavior 1 - Conditioned Section |
| 7 | `SECTION_SEQ` | DOUBLE |  |  | sequence of the section on the form |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

