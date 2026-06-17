# CASSETTE

> This activity table contains entries for blocks that are created from specimens. Parameters such as the specimen, block/cassette identification code, fixative, and number of pieces of tissue are included.

**Description:** Cassette  
**Table type:** ACTIVITY  
**Primary key:** `CASSETTE_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CASE_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case and specimen information stored on the CASE_SPECIMEN activity table. |
| 2 | `CASSETTE_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row included on the CASSETTE table (block/cassette). This field would be used to join to other tables (as a foreign key) such as the SLIDE table. |
| 3 | `CASSETTE_TAG_ID` | DOUBLE | NOT NULL | FK→ | This field contains an identifier referencing the block/cassette identification code associated with the block/cassette. |
| 4 | `DISCARD_DT_TM` | DATETIME |  |  | The date and time the block was disposed. |
| 5 | `DISCARD_REASON_CD` | DOUBLE | NOT NULL |  | The reason why the block was disposed. |
| 6 | `EMBEDDING_MEDIA_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 7 | `FIXATIVE_CD` | DOUBLE | NOT NULL |  | If the block/cassette was associated with a fixative, this field includes the identification code associated with the fixative. Fixatives are stored on codeset 1302. |
| 8 | `FROZEN_IND` | DOUBLE |  |  | This field is not used at this time. |
| 9 | `LABEL_CREATE_DT_TM` | DATETIME |  |  | The date and time the last label was created. |
| 10 | `LABEL_CREATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of method used to creat the label.0 = Spooled,1 = Flat File3 = Nice Label Flat File |
| 11 | `ON_LOAN_LOCN_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 12 | `ORIGINAL_STORAGE_DT_TM` | DATETIME |  |  | The date and time the block was placed in storage. |
| 13 | `ORIGIN_MODIFIER` | CHAR(7) |  |  | If a block modifier value was associated with the processing task that caused the row to be added to the CASSETTE table, the modifier value entered by the user is stored in this field. |
| 14 | `OWNER_ID` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 15 | `PIECES` | CHAR(3) |  |  | If a number of pieces value was associated with the processing task that cause the row to be added to the CASSETTE table, the number of pieces value entered by the user is stored in this field. The order entry applications default this value to 1. |
| 16 | `SECTIONABLE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 17 | `STORAGE_LOCATION_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 18 | `SUPPLEMENTAL_TAG` | CHAR(2) |  |  | This field is not used at this time. |
| 19 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field stores the internal identification code associated with the discrete task that caused the row to be added to the CASSETTE table. This value could be used to join to the discrete task assay tables. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_SPECIMEN_ID` | [CASE_SPECIMEN](CASE_SPECIMEN.md) | `CASE_SPECIMEN_ID` |
| `CASSETTE_TAG_ID` | [AP_TAG](AP_TAG.md) | `TAG_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PROCESSING_TASK](PROCESSING_TASK.md) | `CASSETTE_ID` |
| [SLIDE](SLIDE.md) | `CASSETTE_ID` |

