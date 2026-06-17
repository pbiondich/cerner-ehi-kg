# CSM_REQUESTS_ARCHIVE

> This table will hold the requests purged from the CSM_REQUESTS table.

**Description:** CSM REQUESTS ARCHIVE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPL_PRSNL_ID` | DOUBLE | NOT NULL |  | Person who updated the request last from the UPDT_ID on the CSM_REQUESTS table. |
| 2 | `CONTACT` | VARCHAR(100) |  |  | Name of last person contacted at time of Purge for that requests. Comes form CSM_LST_CONTACT table. |
| 3 | `CSM_AD_HOC_EXT` | CHAR(100) |  |  | Ad Hoc phon number extension from CSM_AD_HOCS table. |
| 4 | `CSM_AD_HOC_PHONE` | CHAR(100) |  |  | Ad Hoc phone number from CSM_AD_HOCS table. |
| 5 | `CSM_CAT_ID` | DOUBLE | NOT NULL | FK→ | Request Category Identifier from CSM_REQUESTS table. |
| 6 | `CSM_COMPL_DT_TM` | DATETIME |  |  | Date and Time the Request was completed from CSM_REQUESTS table. |
| 7 | `CSM_DUE_DT_TM` | DATETIME |  |  | The original due date of the request from the CSM_REQUESTS table. |
| 8 | `CSM_ORD_DT_TM` | DATETIME |  |  | The original order date and time of the request from the CSM_REQUESTS table. |
| 9 | `CSM_PHONE_STAT_DESC` | CHAR(40) |  |  | The phone description of the call back number at the time of the purge for the request from the CSM_REQUESTS table. |
| 10 | `CSM_PRIOR_ID` | DOUBLE | NOT NULL | FK→ | CSM Request Piority Identifier from the CSM_REQUESTS table. |
| 11 | `CSM_REQ_ID` | DOUBLE | NOT NULL |  | The unique request identifier from the CSM_REQUESTS table. |
| 12 | `CSM_SUB_CAT_ID` | DOUBLE | NOT NULL | FK→ | Request Sub-Category identifier for the request from the CSM_REQUESTS table. |
| 13 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location for the Request from the CSM_REQUEST table. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization for the Request from the CSM_REQUESTS table. |
| 15 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique Identifier on table listed in PARENT_ENTITY_NAME. |
| 16 | `PARENT_ENTITY_NAME` | CHAR(32) |  |  | Location of name of Parent Table of Parent_Entity_Id |
| 17 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the phone number |
| 18 | `PURGED_DT_TM` | DATETIME |  |  | Date and time the request was purged. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CSM_CAT_ID` | [CSM_CATEGORIES](CSM_CATEGORIES.md) | `CSM_CAT_ID` |
| `CSM_PRIOR_ID` | [CSM_PRIORITIES](CSM_PRIORITIES.md) | `CSM_PRIOR_ID` |
| `CSM_SUB_CAT_ID` | [CSM_SUB_CATEGORIES](CSM_SUB_CATEGORIES.md) | `CSM_SUB_CAT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |

