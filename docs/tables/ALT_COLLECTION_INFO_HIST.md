# ALT_COLLECTION_INFO_HIST

> History of alternate collection requirements for a particular collection requirement on an orderable.

**Description:** Alternate Collection Information History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_COLLECTION_INFO_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies historical alternate container information. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the order catalog item associated with the collection requirements. |
| 3 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the collection class associated with the alternate container. If this value is null then the collection class of the parent collection requirement should be used. |
| 4 | `COLL_INFO_HIST_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Collection History Information |
| 5 | `MIN_VOL_AMT` | DOUBLE | NOT NULL |  | The numeric value which, along with the specim container's Units, defines the smallest amount of specimen needed for the alternate. |
| 6 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the specimen type associated with the collection requirements. |
| 7 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the specimen container associated with the alternate container. |
| 8 | `SPEC_HNDL_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the special handling instructions associated with the alternate container. If this value is NULL then the special handling instructions of the parent collection requirement should be used. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLL_INFO_HIST_ID` | [COLLECTION_INFO_QUAL_HIST](COLLECTION_INFO_QUAL_HIST.md) | `COLLECTION_INFO_QUAL_HIST_ID` |

