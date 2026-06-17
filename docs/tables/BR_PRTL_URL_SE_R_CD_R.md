# BR_PRTL_URL_SE_R_CD_R

> Stores the relationship between portal url relations and codes. Portal urls which are related to CCNs or Eligible Providers need to have event codes tied to those .relationships, in order to pull data if certain events occur.

**Description:** Bedrock Portal URL Service Entity Relationship Code Relation  
**Table type:** REFERENCE  
**Primary key:** `BR_PRTL_URL_SE_R_CD_R_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_PORTAL_URL_SVC_ENTITY_R_ID` | DOUBLE | NOT NULL | FK→ | The primary key from the br_portal_url_svc_entity_r table. Indicates the portal relationship to which these codes are being tied. |
| 4 | `BR_PRTL_URL_SE_R_CD_R_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_PRTL_URL_SE_R_CD_R table. |
| 5 | `CODE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of the code value being tied to the relationship. Can be different for codes from the same code_set. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `ORIG_PRTL_URL_SE_R_CD_R_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the value of the PK for a particular set of rows in BR_PRTL_URL_SE_R_CD_R. |
| 8 | `PORTAL_ATTR_CD_VALUE` | DOUBLE | NOT NULL |  | The code value being tied to the portal relationship. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_PORTAL_URL_SVC_ENTITY_R_ID` | [BR_PORTAL_URL_SVC_ENTITY_R](BR_PORTAL_URL_SVC_ENTITY_R.md) | `BR_PORTAL_URL_SVC_ENTITY_R_ID` |
| `ORIG_PRTL_URL_SE_R_CD_R_ID` | [BR_PRTL_URL_SE_R_CD_R](BR_PRTL_URL_SE_R_CD_R.md) | `BR_PRTL_URL_SE_R_CD_R_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_PRTL_URL_SE_R_CD_R](BR_PRTL_URL_SE_R_CD_R.md) | `ORIG_PRTL_URL_SE_R_CD_R_ID` |

