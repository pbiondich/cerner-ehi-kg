# RCA_MOBILE_PROFILE

> Defines a profile to be usied by the registration kiosk.

**Description:** Revenue Cycle Mobile Profile  
**Table type:** REFERENCE  
**Primary key:** `RCA_MOBILE_PROFILE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_SOURCE_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This column was replaced by mobile_profile_type_cd |
| 3 | `FACILITY_ORG_ID` | DOUBLE | NOT NULL | FK→ | Associates a profile to an organization. |
| 4 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 5 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related long blob |
| 6 | `MOBILE_PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the source feed for the data from which the row was populated. This is mainly used to determine the exact application source for data. Ex. Mobile Kiosk, Esig. |
| 7 | `PROFILE_NAME` | VARCHAR(100) | NOT NULL |  | Name of the profile |
| 8 | `PROFILE_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | type of profile, ESIG or KIOSK |
| 9 | `RCA_MOBILE_PROFILE_ID` | DOUBLE | NOT NULL | PK | Uniquely a profile to be used by the registration kiosk. |
| 10 | `SCHEMA_VERSION_NBR` | DOUBLE | NOT NULL |  | The schema version number for the mobile kiosk profile. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCA_MOBILE_SESSION](RCA_MOBILE_SESSION.md) | `RCA_MOBILE_PROFILE_ID` |

