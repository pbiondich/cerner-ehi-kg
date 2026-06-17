# SI_EXTERNAL_SERVICE

> Table containing defined external services

**Description:** SI External Service  
**Table type:** REFERENCE  
**Primary key:** `SI_EXTERNAL_SERVICE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORIZATION_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type of authorization this service uses. |
| 2 | `CERTIFICATE_TXT` | VARCHAR(255) |  |  | The certificate text or password used to sign in the user provided in the username column. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `EXTERNAL_SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of service utilized for this system. |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 6 | `SERVICE_NAME` | VARCHAR(255) | NOT NULL |  | Name of the service defiend by the row. Should be unique within a given external service type. |
| 7 | `SERVICE_URI` | VARCHAR(512) |  |  | The Universal Service Identifier where the service is located |
| 8 | `SI_EXTERNAL_SERVICE_ID` | DOUBLE | NOT NULL | PK | Unique generated number - identifies a single row in the table |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `USERNAME_TXT` | VARCHAR(100) |  |  | The user name to use for authorizating with the service if the service uses a username and password authorization model |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_EXTERNAL_SERVICE_VOCAB](SI_EXTERNAL_SERVICE_VOCAB.md) | `SI_EXTERNAL_SERVICE_ID` |
| [SI_SERVICE_RELTN](SI_SERVICE_RELTN.md) | `SI_EXTERNAL_SERVICE_ID` |

