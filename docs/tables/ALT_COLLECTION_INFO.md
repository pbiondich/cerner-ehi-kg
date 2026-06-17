# ALT_COLLECTION_INFO

> Defines alternate collection requirements for a prticular collection requirement on an orderable.

**Description:** Alternate Collections Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_COLLECTION_INFO_ID` | DOUBLE | NOT NULL |  | Uniquely identifies alternate collection requirements information. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The internal number assigned by the system to the order catalog item associated with the collection requirements. |
| 3 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Collection Class associated with the alternate container. |
| 4 | `COLL_INFO_SEQ` | DOUBLE | NOT NULL | FK→ | The sequence with which the collection requirements are associated. |
| 5 | `MIN_VOL_AMT` | DOUBLE | NOT NULL |  | The numeric value which, along with the specimen container's Units, defines the smallest amount of specimen needed for the alternate collection requirements. |
| 6 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The internal number assigned by the system to the Specimen Type associated with the collection requirements. |
| 7 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Specimen Container associated with the collection requirements. |
| 8 | `SPEC_HNDL_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Special Handling instructions associated with the alternate container. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [COLLECTION_INFO_QUALIFIERS](COLLECTION_INFO_QUALIFIERS.md) | `CATALOG_CD` |
| `COLL_INFO_SEQ` | [COLLECTION_INFO_QUALIFIERS](COLLECTION_INFO_QUALIFIERS.md) | `SEQUENCE` |
| `SPECIMEN_TYPE_CD` | [COLLECTION_INFO_QUALIFIERS](COLLECTION_INFO_QUALIFIERS.md) | `SPECIMEN_TYPE_CD` |

