# SI_INTEROP_AUTHOR

> This table holds information about authors of documents that have metadata in the SI_INTEROP_METADATA table

**Description:** System Integration Advanced Interoperability Author  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of the author in the metadata author list. |
| 2 | `FULL_NAME_FRMT` | VARCHAR(255) |  |  | The authors full formatted name. |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel if this author has been added to Millennium. |
| 4 | `SI_INTEROP_AUTHOR_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `SI_INTEROP_METADATA_ID` | DOUBLE | NOT NULL | FK→ | The SI_INTEROP_METADATA with this author. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SI_INTEROP_METADATA_ID` | [SI_INTEROP_METADATA](SI_INTEROP_METADATA.md) | `SI_INTEROP_METADATA_ID` |

