# UCMR_WORKSHEET_ORDERABLE_R

> This table stores relationships between worksheets and orderables.

**Description:** Unified Case Management Reference Worksheet Orderable Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field is used to store the internal code for the order catalog item. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies which containers created in the workup should be associated with this order. |
| 7 | `SPECIMEN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates what specimen(s) are associated with the orderable: 0- The specific specimen in the specimen_type_cd field, 1 - All workup containers, or 2 - No specimens. |
| 8 | `UCMR_WORKSHEET_ID` | DOUBLE | NOT NULL | FK→ | This field contains a unique identifier for the associated worksheet. |
| 9 | `UCMR_WORKSHEET_ORDERABLE_R_ID` | DOUBLE | NOT NULL |  | Identifies a unique relationship between a worksheet and an orderable. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_WORKSHEET_ID` | [UCMR_WORKSHEET](UCMR_WORKSHEET.md) | `UCMR_WORKSHEET_ID` |

