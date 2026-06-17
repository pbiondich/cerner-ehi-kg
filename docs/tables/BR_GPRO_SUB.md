# BR_GPRO_SUB

> A client-defined sub-group of a BR_GPRO group.

**Description:** Bedrock Group Provider Reporting Option Subgroup  
**Table type:** REFERENCE  
**Primary key:** `BR_GPRO_SUB_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_GPRO_ID` | DOUBLE |  | FK→ | Identifies the group associated to the subgroup. Foreign key to BR_GRO table. |
| 4 | `BR_GPRO_SUB_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_GPRO_SUB table. |
| 5 | `BR_GPRO_SUB_NAME` | VARCHAR(255) |  |  | The name given to the subgroup by a client. |
| 6 | `BR_GPRO_SUB_NBR_TXT` | VARCHAR(50) |  |  | User-entered alphanumeric value for the subgroup number. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `ORIG_BR_GPRO_SUB_ID` | DOUBLE |  | FK→ | Used for versioning. Contains the original PK from BR_GPRO_SUB |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_GPRO_ID` | [BR_GPRO](BR_GPRO.md) | `BR_GPRO_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_BR_GPRO_SUB_ID` | [BR_GPRO_SUB](BR_GPRO_SUB.md) | `BR_GPRO_SUB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_GPRO_SUB](BR_GPRO_SUB.md) | `ORIG_BR_GPRO_SUB_ID` |
| [BR_GPRO_SUB_RELTN](BR_GPRO_SUB_RELTN.md) | `BR_GPRO_SUB_ID` |

