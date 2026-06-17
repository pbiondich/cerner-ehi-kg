# BR_GPRO_RELTN

> Stores the relationship between GPROs, eligible providers and locations

**Description:** Bedrock Group Provider Reporting Option Relation  
**Table type:** REFERENCE  
**Primary key:** `BR_GPRO_RELTN_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACI_EXCLUDED_IND` | DOUBLE | NOT NULL |  | Identifies a TIN relation that should be excluded from ACI (Advancing Care Information) reporting |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BR_GPRO_ID` | DOUBLE | NOT NULL | FK→ | The GPRO that this provider is associated with. |
| 8 | `BR_GPRO_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the br_gpro_reltn table. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `ORIG_BR_GPRO_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the original PK from BR_GPRO_RELTN |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The provider that is a part of this GPRO. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table that is the source of information for the parent_entity_id column. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_GPRO_ID` | [BR_GPRO](BR_GPRO.md) | `BR_GPRO_ID` |
| `ORIG_BR_GPRO_RELTN_ID` | [BR_GPRO_RELTN](BR_GPRO_RELTN.md) | `BR_GPRO_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_GPRO_RELTN](BR_GPRO_RELTN.md) | `ORIG_BR_GPRO_RELTN_ID` |

