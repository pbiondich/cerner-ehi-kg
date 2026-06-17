# RCM_POST_ACUTE_PROVIDER

> Stores post-acute provider information.

**Description:** RevWorks Care Management Post Acute Provider  
**Table type:** REFERENCE  
**Primary key:** `RCM_POST_ACUTE_PROVIDER_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CITY` | VARCHAR(100) | NOT NULL |  | The city of the post-acute provider. |
| 3 | `PHONE` | VARCHAR(100) | NOT NULL |  | The phone number of the post-acute provider. |
| 4 | `POSTAL_CODE` | VARCHAR(25) | NOT NULL |  | The postal code of the post-acute provider. |
| 5 | `PROVIDER_IDENT` | VARCHAR(100) | NOT NULL |  | This is the value of the external unique identifier of the post-acute provider. |
| 6 | `PROVIDER_NAME` | VARCHAR(100) | NOT NULL |  | The name of the post-acute provider. |
| 7 | `RCM_POST_ACUTE_PROVIDER_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies post-acute provider information. |
| 8 | `STATE` | VARCHAR(100) | NOT NULL |  | The state of the post-acute provider. |
| 9 | `STREET_ADDR` | VARCHAR(100) | NOT NULL |  | Contains line one of the street address of the post-acute provider. |
| 10 | `STREET_ADDR2` | VARCHAR(100) | NOT NULL |  | Contains line two of the street address of the post-acute provider. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ENCNTR_AVOIDABLE_DAYS](ENCNTR_AVOIDABLE_DAYS.md) | `POST_ACUTE_PROVIDER_ID` |
| [ENCNTR_READMIT_ASSESS](ENCNTR_READMIT_ASSESS.md) | `POST_ACUTE_PROVIDER_ID` |
| [RCM_POST_ACUTE_EVENT](RCM_POST_ACUTE_EVENT.md) | `POST_ACUTE_PROVIDER_ID` |
| [RCM_POST_ACUTE_PROV_EMAIL](RCM_POST_ACUTE_PROV_EMAIL.md) | `RCM_POST_ACUTE_PROVIDER_ID` |

