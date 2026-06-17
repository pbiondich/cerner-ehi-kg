# PFT_PAYMENT_LOCATION_DEF

> Stores the definition of a payment location.

**Description:** Payment Location Definition  
**Table type:** REFERENCE  
**Primary key:** `PFT_PAYMENT_LOCATION_DEF_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DEFAULT_PAYMENT_LOC_IND` | DOUBLE | NOT NULL |  | This option will allow the user to keep the previous payment location as default payment location in upcoming payments |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `ORIG_PAYMENT_LOCATION_DEF_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the payment location definition information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 10 | `PAYMENT_LOCATION_DESC` | VARCHAR(255) | NOT NULL |  | The textual description of the Payment Location |
| 11 | `PAYMENT_LOCATION_NAME` | VARCHAR(255) | NOT NULL |  | The name of the payment location |
| 12 | `PAYMENT_LOCATION_NAME_KEY` | VARCHAR(255) | NOT NULL |  | The name of the Payment Location in uppercases with all spaces and special characters removed. |
| 13 | `PFT_PAYMENT_LOCATION_DEF_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PFT_PAYMENT_LOCATION_DEF table. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_PAYMENT_LOCATION_DEF_ID` | [PFT_PAYMENT_LOCATION_DEF](PFT_PAYMENT_LOCATION_DEF.md) | `PFT_PAYMENT_LOCATION_DEF_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_PAYMENT_LOCATION](PFT_PAYMENT_LOCATION.md) | `PFT_PAYMENT_LOCATION_DEF_ID` |
| [PFT_PAYMENT_LOCATION_DEF](PFT_PAYMENT_LOCATION_DEF.md) | `ORIG_PAYMENT_LOCATION_DEF_ID` |

