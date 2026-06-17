# PROCEDURE_SPECIMEN_TYPE

> Tells you what specimen types a given Lab orderable can be performed on.

**Description:** Procedure Specimen Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_CLASS_CD` | DOUBLE | NOT NULL | FK→ | The system generated number that uniquely identifies the accession class. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The system generated number that uniquely identifies the order catalog item. |
| 3 | `DEFAULT_COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The system generated number that uniquely identifies the collection method code. This represents the default collection method for the order catalog item/specimen type. |
| 4 | `DEFAULT_IND` | DOUBLE |  |  | not currently used |
| 5 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | System generated number that uniquely identifies the specimen type. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_CLASS_CD` | [ACCESSION_CLASS](ACCESSION_CLASS.md) | `ACCESSION_CLASS_CD` |

