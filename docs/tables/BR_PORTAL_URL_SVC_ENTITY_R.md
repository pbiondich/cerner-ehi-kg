# BR_PORTAL_URL_SVC_ENTITY_R

> This will hold the relationships between a portal url and a group of CCN's and/or a group of Eligible Providers

**Description:** Bedrock Portal URL Service Entity Relation  
**Table type:** REFERENCE  
**Primary key:** `BR_PORTAL_URL_SVC_ENTITY_R_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_PORTAL_URL_ID` | DOUBLE | NOT NULL | FK→ | The portal URL that this service entity is related to. |
| 4 | `BR_PORTAL_URL_SVC_ENTITY_R_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_PORTAL_URL_SVC_ENTITY_R table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The will hold the unique identifier to the table stored in parent_entity_name |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | This will hold the table name of the type of service entity, whether it be BR_ELIGIBLE_PROVIDER, or BR_CCN, or CODE_VALUE |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_PORTAL_URL_ID` | [BR_PORTAL_URL](BR_PORTAL_URL.md) | `BR_PORTAL_URL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_PRTL_URL_SE_R_CD_R](BR_PRTL_URL_SE_R_CD_R.md) | `BR_PORTAL_URL_SVC_ENTITY_R_ID` |

