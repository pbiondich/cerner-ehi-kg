# CODE_VALUE_EVENT_R

> Used to alias code_values to event codes.

**Description:** CODE VALUE EVENT R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_CD` | DOUBLE | NOT NULL |  | event_cd to be used to post clinical_event recordColumn |
| 2 | `FLEX1_CD` | DOUBLE | NOT NULL |  | Used to flex the parent_cd field. Should be 0 if no flexing required. This would allow the same catalog_cd to point to multiple event_cd's based on some other criteria (i.e. specimen_type_cd). |
| 3 | `FLEX2_CD` | DOUBLE | NOT NULL |  | Used to flex the parent_cd field. Should be 0 if no flexing required. This would allow the same catalog_cd to point to multiple event_cd's based on some other criteria (i.e. specimen_type_cd). |
| 4 | `FLEX3_CD` | DOUBLE | NOT NULL |  | Used to flex the parent_cd field. Should be 0 if no flexing required. This would allow the same catalog_cd to point to multiple event_cd's based on some other criteria (i.e. specimen_type_cd). |
| 5 | `FLEX4_CD` | DOUBLE | NOT NULL |  | Used to flex the parent_cd field. Should be 0 if no flexing required. This would allow the same catalog_cd to point to multiple event_cd's based on some other criteria (i.e. specimen_type_cd). |
| 6 | `FLEX5_CD` | DOUBLE | NOT NULL |  | Used to flex the parent_cd field. Should be 0 if no flexing required. This would allow the same catalog_cd to point to multiple event_cd's based on some other criteria (i.e. specimen_type_cd). |
| 7 | `PARENT_CD` | DOUBLE | NOT NULL |  | This is the code_value of the thing we are mapping to an event_cd. It can be a dta_cd, orc_cd, or a code_value. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

