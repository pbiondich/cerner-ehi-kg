# BB_QC_GROUP_XREF

> This table maintains a list of Blood Bank QC cross-reference groups.

**Description:** Blood Bank Quality Control Group Cross Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the QC group being cross-referenced from. (BB_QC_GROUP) |
| 2 | `GROUP_XREF_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies the QC group cross-reference |
| 3 | `RELATED_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the QC group being cross-referenced to. (BB_QC_GROUP) |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |
| `RELATED_GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |

