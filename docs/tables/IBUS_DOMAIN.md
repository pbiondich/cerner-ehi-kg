# IBUS_DOMAIN

> Details about an iBus (An iBus is a platform that is used to communicate between devices and millennium.)

**Description:** iBus Domain  
**Table type:** REFERENCE  
**Primary key:** `IBUS_DOMAIN_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IBUS_CONNECTION_TYPE_TXT` | VARCHAR(255) |  |  | The iBus connection metadata. |
| 2 | `IBUS_DOMAIN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the ibus_domain table. |
| 3 | `IBUS_DOMAIN_NAME` | VARCHAR(255) | NOT NULL |  | Name of the ibus domain |
| 4 | `IBUS_JSON_WEB_KEY_TXT` | VARCHAR(4000) |  |  | RFC 7517 JSON Web Key for iBus web connection authentication. |
| 5 | `IBUS_TENANT_IDENT` | VARCHAR(255) |  |  | Unique identfier of a Tenant in an iBus Cloud Domain. |
| 6 | `JNDI_URL` | VARCHAR(255) | NOT NULL |  | Fully qualified DNS address for the ibus installation |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MILLENNIUM_DOMAIN_NAME` | VARCHAR(255) | NOT NULL |  | The millennium domain name associated to the defined ibus |
| 9 | `RECEIVE_ALERTS_IND` | DOUBLE | NOT NULL |  | Indicator that states whether the defined ibus will receive ENS alerts |
| 10 | `SEND_FORMULARY_UPDATES_IND` | DOUBLE | NOT NULL |  | Indicator that states whether the defined ibus will send formulary updates |
| 11 | `SEND_PHARMACY_DEVICE_IND` | DOUBLE | NOT NULL |  | Indicator that states whether the defined ibus will send worklist information to Talyst. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `WORKFLOW_LABELS_TXT` | VARCHAR(255) |  |  | Labels to be used to identify workflows associated with this domain |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [IBUS_DOMAIN_ADM_DOMAIN](IBUS_DOMAIN_ADM_DOMAIN.md) | `IBUS_DOMAIN_ID` |

