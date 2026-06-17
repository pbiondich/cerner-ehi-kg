# ACCESSION_CLASS

> All accession classes (codeset 2056) are stored in this table with their corresponding accession format.

**Description:** Accession Class  
**Table type:** REFERENCE  
**Primary key:** `ACCESSION_CLASS_CD`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_CLASS_CD` | DOUBLE | NOT NULL | PK | The internal number assigned by the system as a code value for the Accession Class. |
| 2 | `ACCESSION_FORMAT_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Accession Format to be assigned to orders having this Accession Class. |
| 3 | `GROUP_IND` | DOUBLE | NOT NULL |  | Indicates whether the accession class is to be used as a group identifier for linking patient orders. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROCEDURE_SPECIMEN_TYPE](PROCEDURE_SPECIMEN_TYPE.md) | `ACCESSION_CLASS_CD` |

