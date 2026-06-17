# PCS_LOT_INFORMATION

> This table stores the individual lot information for all lots received into inventory.

**Description:** PathNet Common Services Lot Information  
**Table type:** ACTIVITY  
**Primary key:** `LOT_INFORMATION_ID`  
**Columns:** 19  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the LONG_TEXT row that contains the lot comment text. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXEMPT_IND` | DOUBLE | NOT NULL |  | This field indicates whether a lot is exempt from QC testing. |
| 5 | `EXPIRE_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time that a lot is scheduled to expire. |
| 6 | `KIT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the associated PCS_KIT_INFORMATION row. This field will only be used if the lot was built as part of a kit. |
| 7 | `LOT_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the associated PCS_LOT_DEFINITION row. |
| 8 | `LOT_IDENT` | VARCHAR(40) | NOT NULL |  | This field contains the user-defined lot "number" as defined by the supplier. |
| 9 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL | PK | This field contains the unique identifier of the specific lot information. |
| 10 | `LOT_SOURCE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier to the original PCS_LOT_INFORMATION row associated with the lot. This allows history to be tracked for a given lot. |
| 11 | `RECEIVED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date/time the lot was received. |
| 12 | `RECEIVED_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that received the lot. |
| 13 | `RECEIVED_QTY_NBR` | DOUBLE | NOT NULL |  | This field contains the number of items received in the associated lot. |
| 14 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the status associated with the lot. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `KIT_INFORMATION_ID` | [PCS_KIT_INFORMATION](PCS_KIT_INFORMATION.md) | `KIT_INFORMATION_ID` |
| `LOT_DEFINITION_ID` | [PCS_LOT_DEFINITION](PCS_LOT_DEFINITION.md) | `LOT_DEFINITION_ID` |
| `RECEIVED_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [BB_QC_GRP_REAGENT_LOT](BB_QC_GRP_REAGENT_LOT.md) | `LOT_INFORMATION_ID` |
| [MIC_BIOCHEMICAL_TEST_RESULT](MIC_BIOCHEMICAL_TEST_RESULT.md) | `GROUP_LOT_INFORMATION_ID` |
| [MIC_BIOCHEMICAL_TEST_RESULT](MIC_BIOCHEMICAL_TEST_RESULT.md) | `LOT_INFORMATION_ID` |
| [MIC_MEDIA_LOT_RELTN](MIC_MEDIA_LOT_RELTN.md) | `LOT_INFORMATION_ID` |
| [MIC_QC_RESULT](MIC_QC_RESULT.md) | `ITEM_LOT_INFO_ID` |
| [MIC_QC_RESULT_SCHEDULE](MIC_QC_RESULT_SCHEDULE.md) | `COMPNT_LOT_INFO_ID` |
| [MIC_SUS_MED_RESULT](MIC_SUS_MED_RESULT.md) | `LOT_INFORMATION_ID` |
| [RESULT](RESULT.md) | `LOT_INFORMATION_ID` |

