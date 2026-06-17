# PFT_PAYMENT_LOCATION

> This table will store client defined location where payments are collected.

**Description:** ProFit Paymnet Location  
**Table type:** REFERENCE  
**Primary key:** `PFT_PAYMENT_LOCATION_ID`  
**Columns:** 20  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the organization related to this payment location. |
| 11 | `PAYMENT_LOCATION_DESCRIPTION` | VARCHAR(255) |  |  | ** Obsolete ** Contains a textual description of the payment location. ** This column is no longer being used ** |
| 12 | `PAYMENT_LOCATION_NAME` | VARCHAR(255) | NOT NULL |  | ** Obsolete ** Free text value for the name of the location or drawer. ** This column is no longer being used ** |
| 13 | `PAYMENT_LOCATION_NAME_KEY` | VARCHAR(255) | NOT NULL |  | ** Obsolete ** Contains the payment location name in upper case with all spaces and symbols removed. ** This column is no longer being used ** |
| 14 | `PFT_PAYMENT_LOCATION_DEF_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the PFT_PAYMENT_LOCATION_DEF table. |
| 15 | `PFT_PAYMENT_LOCATION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a payment location. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PFT_PAYMENT_LOCATION_DEF_ID` | [PFT_PAYMENT_LOCATION_DEF](PFT_PAYMENT_LOCATION_DEF.md) | `PFT_PAYMENT_LOCATION_DEF_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `PFT_PAYMENT_LOCATION_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `PFT_PAYMENT_LOCATION_ID` |
| [INTERFACE_TRANSACTION](INTERFACE_TRANSACTION.md) | `PFT_PAYMENT_LOCATION_ID` |
| [TRANS_LOG](TRANS_LOG.md) | `PFT_PAYMENT_LOCATION_ID` |

