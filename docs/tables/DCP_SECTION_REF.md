# DCP_SECTION_REF

> Contains the defintion of a single form section such as display.

**Description:** Section Definition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. For a single dcp_input_ref_id there will be at most active row, which means the end_effective_dt_tm is indefinite. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this version of the section is effective. |
| 3 | `DCP_SECTION_INSTANCE_ID` | DOUBLE | NOT NULL |  | Unique identifier for individual versions of the section. |
| 4 | `DCP_SECTION_REF_ID` | DOUBLE | NOT NULL |  | Unique identifier for each individual form section |
| 5 | `DEFINITION` | VARCHAR(200) |  |  | Textual definition of the section |
| 6 | `DESCRIPTION` | VARCHAR(200) |  |  | Textual description of the section. This is displayed in the navigator when a form is charted. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which this version of the section is no longer effective. |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | associated event code for the section. Currently not used. |
| 9 | `HEIGHT` | DOUBLE |  |  | Height of section. |
| 10 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | associated task_assay_cd. Currently not used |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `WIDTH` | DOUBLE |  |  | Width of section. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

