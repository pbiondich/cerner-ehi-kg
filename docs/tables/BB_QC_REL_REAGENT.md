# BB_QC_REL_REAGENT

> This table maintains a list of reagent relationships that can be used in a quality control group.

**Description:** Blood Bank Quality Control Related Reagent  
**Table type:** REFERENCE  
**Primary key:** `RELATED_REAGENT_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `REAGENT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the reagent. |
| 3 | `RELATED_REAGENT_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the reagent relationship. |
| 4 | `RELATED_REAGENT_NAME` | VARCHAR(40) | NOT NULL |  | This field contains the name of the related reagent. |
| 5 | `RELATED_REAGENT_NAME_KEY` | VARCHAR(40) | NOT NULL |  | This field contains the name of the related reagent in uppercase with spaces and special characters removed. |
| 6 | `RELATED_REAGENT_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | RELATED_REAGENT_NAME_KEY_A_NLS column |
| 7 | `RELATED_REAGENT_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | This field contains the corresponding non-English character set values for the _KEY column. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BB_QC_GRP_REAGENT_LOT](BB_QC_GRP_REAGENT_LOT.md) | `RELATED_REAGENT_ID` |
| [BB_QC_REL_REAGENT_DETAIL](BB_QC_REL_REAGENT_DETAIL.md) | `RELATED_REAGENT_ID` |

