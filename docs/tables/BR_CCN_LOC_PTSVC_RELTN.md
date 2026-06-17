# BR_CCN_LOC_PTSVC_RELTN

> Stores point of service information associated to locations that are associated to CCNs.

**Description:** Bedrock DMS Certification Number Location Point of Service Relation  
**Table type:** REFERENCE  
**Primary key:** `BR_CCN_LOC_PTSVC_RELTN_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CCN_LOC_PTSVC_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_CCN_LOC_PTSVC_RELTN table. |
| 4 | `BR_CCN_LOC_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The Location and CCN that this Point of Service Code and Encounter Type pertain to. |
| 5 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the encounter associated encounter type. The combination of point of service, encounter type, and location drive how the data is submitted to CMS. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `ORIG_BR_CCN_LOC_PTSVC_R_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the original PK from BR_CCN_LOC_PTSVC_RELTN |
| 8 | `PTSVC_CODE_NBR` | DOUBLE | NOT NULL |  | Stores the point of service code used on professional claims to specify the entity where service(s) were rendered. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_CCN_LOC_RELTN_ID` | [BR_CCN_LOC_RELTN](BR_CCN_LOC_RELTN.md) | `BR_CCN_LOC_RELTN_ID` |
| `ORIG_BR_CCN_LOC_PTSVC_R_ID` | [BR_CCN_LOC_PTSVC_RELTN](BR_CCN_LOC_PTSVC_RELTN.md) | `BR_CCN_LOC_PTSVC_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_CCN_LOC_PTSVC_RELTN](BR_CCN_LOC_PTSVC_RELTN.md) | `ORIG_BR_CCN_LOC_PTSVC_R_ID` |

