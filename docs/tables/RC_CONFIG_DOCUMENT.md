# RC_CONFIG_DOCUMENT

> This table will define a configuration document.

**Description:** Revenue Cycle Configuration Document  
**Table type:** REFERENCE  
**Primary key:** `RC_CONFIG_DOCUMENT_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DOCUMENT_VERSION_UUID` | VARCHAR(36) | NOT NULL |  | Uniquely identifies a document version across all domains. |
| 4 | `DOCUMENT_XML_BLOB` | LONGBLOB |  |  | This column stores a related XML document. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the last person to update this configuration document. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `ORIG_RC_CONFIG_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the configuration document information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `RC_CONFIG_DOCUMENT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_CONFIG_DOCUMENT table. |
| 10 | `RC_CONFIG_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RC_CONFIG_PROFILE table. |
| 11 | `RC_CONFIG_SUBSYSTEM_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RC_CONFIG_SUBSYSTEM |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_RC_CONFIG_DOCUMENT_ID` | [RC_CONFIG_DOCUMENT](RC_CONFIG_DOCUMENT.md) | `RC_CONFIG_DOCUMENT_ID` |
| `RC_CONFIG_PROFILE_ID` | [RC_CONFIG_PROFILE](RC_CONFIG_PROFILE.md) | `RC_CONFIG_PROFILE_ID` |
| `RC_CONFIG_SUBSYSTEM_ID` | [RC_CONFIG_SUBSYSTEM](RC_CONFIG_SUBSYSTEM.md) | `RC_CONFIG_SUBSYSTEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CONFIG_DOCUMENT](RC_CONFIG_DOCUMENT.md) | `ORIG_RC_CONFIG_DOCUMENT_ID` |

