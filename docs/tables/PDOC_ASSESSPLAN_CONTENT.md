# PDOC_ASSESSPLAN_CONTENT

> Used to link the assessment-and-plan ; workflow component content to clinical events.

**Description:** Physician Documentation Assesment Plan Content  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | Reference to the CLINICAL_EVENT.EVENT_ID. ; Identifier of the document (MDOC) that contains the given diagnosis or comment. |
| 2 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Reference to NOMENCLATURE.NOMENCLATURE_ID. If the value is NULL, the Assessment&Plan comment is referred. |
| 3 | `PDOC_ASSESSPLAN_CONTENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PDOC_ASSESSPLAN_CONTENT table. |
| 4 | `SERVICE_DT_TM` | DATETIME |  |  | Service Date Time of the Document that contains given diagnosis or comment |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

