# EA_DIGITAL_KEYSTORE

> To store the certificates and keystores required as a part of the Swden Newborn workflow

**Description:** EA_DIGITAL_KEYSTORE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_TXT` | VARCHAR(250) | NOT NULL |  | Arbitrary Identifier for stored KeyStore |
| 3 | `CERT_DATA` | VARCHAR(4000) | NOT NULL |  | Encoded string representation of Certificate in private Keystore |
| 4 | `EA_DIGITAL_KEYSTORE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `NOT_AFTER_DT_TM` | DATETIME |  |  | Certificate's Not After value. Issuing the certificate is not valid after this date |
| 6 | `NOT_BEFORE_DT_TM` | DATETIME |  |  | Certificate's Not Before value. Certificate isn't valid before this date |
| 7 | `PK_DATA` | VARCHAR(4000) | NOT NULL |  | private key on private Keystore file |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

