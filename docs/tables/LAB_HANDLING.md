# LAB_HANDLING

> Defines lab handling information for a particular collection requirement on an orderable.

**Description:** Lab Handling  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The internal number assigned by the system to the order catalog item associated with the collection requirements. |
| 2 | `COLL_INFO_SEQ` | DOUBLE | NOT NULL | FK→ | The sequence with which the collection requirements and lab handlings are associated. |
| 3 | `LAB_HANDLING_CD` | DOUBLE | NOT NULL |  | A code used to identify the different ways a container should be handled. |
| 4 | `LAB_HANDLING_ID` | DOUBLE | NOT NULL |  | Uniquely identifies lab handling information for a particular collection requirement on an orderable. |
| 5 | `LAB_HANDLING_ORDER_SEQ` | DOUBLE | NOT NULL |  | A user assigned numeric value that is used to sort lab handling values. |
| 6 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related specimen type. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [COLLECTION_INFO_QUALIFIERS](COLLECTION_INFO_QUALIFIERS.md) | `CATALOG_CD` |
| `COLL_INFO_SEQ` | [COLLECTION_INFO_QUALIFIERS](COLLECTION_INFO_QUALIFIERS.md) | `SEQUENCE` |
| `SPECIMEN_TYPE_CD` | [COLLECTION_INFO_QUALIFIERS](COLLECTION_INFO_QUALIFIERS.md) | `SPECIMEN_TYPE_CD` |

