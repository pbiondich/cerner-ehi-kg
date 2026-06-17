# EA_DIGITAL_CERT

> Represents digital certificates available to tye system

**Description:** DIGITAL CERTIFICATES  
**Table type:** REFERENCE  
**Primary key:** `EA_DIGITAL_CERT_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS` | VARCHAR(250) | NOT NULL |  | ALIAS TEXT |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `COMPROMISED_DT_TM` | DATETIME |  |  | Timestamp indicating when the key pair was flagged as having been compromised |
| 5 | `EA_DIGITAL_CERT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DIGITAL_CERT table |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FINGERPRINT` | VARCHAR(1000) | NOT NULL |  | Base 64 encoded hash of the certificate |
| 8 | `NOT_AFTER_DT_TM` | DATETIME |  |  | Certificate's Not After value. The certificate is not valid after this date/time. |
| 9 | `NOT_BEFORE_DT_TM` | DATETIME |  |  | Certificate's Not Before value. The certificate is not valid before this date/time. |
| 10 | `SUBJECT` | VARCHAR(4000) | NOT NULL |  | SUBJECT MATTER |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EA_DIGITAL_CERT_KEYS](EA_DIGITAL_CERT_KEYS.md) | `EA_DIGITAL_CERT_ID` |

