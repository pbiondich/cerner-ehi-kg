# MP_VIEWPOINT_ENCNTR

> Stores views that are associated with a viewpoint with specific encounter types. For example, for the Inpatient encounter type, the Inpatient Summary is associated

**Description:** MPages Viewpoint Encounter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type associated to this viewpoint. |
| 2 | `MP_VIEWPOINT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MP_VIEWPOINT_ENCNTR table. |
| 3 | `MP_VIEWPOINT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The viewpoint relation row that this encounter type code pertains to. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MP_VIEWPOINT_RELTN_ID` | [MP_VIEWPOINT_RELTN](MP_VIEWPOINT_RELTN.md) | `MP_VIEWPOINT_RELTN_ID` |

