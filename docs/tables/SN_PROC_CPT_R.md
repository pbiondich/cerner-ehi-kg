# SN_PROC_CPT_R

> Procedure / CPT code associations

**Description:** SN PROC CPT R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CPT_SEQ` | DOUBLE | NOT NULL |  | Identifies the priority and sequence in which the CPT was selected |
| 2 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a CPT 4 code |
| 3 | `PRINCIPLE_TYPE_CD` | DOUBLE | NOT NULL |  | The principle type cd from principle type code set |
| 4 | `PROCEDURE_CD` | DOUBLE | NOT NULL | FK→ | Unique identifier for a Surgical procedure |
| 5 | `PROC_CPT_ASSOC_ID` | DOUBLE | NOT NULL |  | Procedure CPT code association identifier |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PROCEDURE_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

