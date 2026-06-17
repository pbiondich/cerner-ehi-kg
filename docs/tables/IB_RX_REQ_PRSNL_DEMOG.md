# IB_RX_REQ_PRSNL_DEMOG

> Stores the demographic information of the personnel of an Inbound RX Request.

**Description:** Inbound Pharmacy Request Personnel Demographic  
**Table type:** ACTIVITY  
**Primary key:** `IB_RX_REQ_PRSNL_DEMOG_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CITY_NAME` | VARCHAR(255) |  |  | The personnel's city name. |
| 2 | `FIRST_NAME` | VARCHAR(255) |  |  | The first name of the personnel. |
| 3 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL | FK→ | The inbound request this personnel is related to. |
| 4 | `IB_RX_REQ_PRSNL_DEMOG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the IB_RX_REQ_PRSNL_DEMOG table. |
| 5 | `LAST_NAME` | VARCHAR(255) |  |  | The personnel's last name. |
| 6 | `MIDDLE_NAME` | VARCHAR(255) |  |  | The personnel's middle name. |
| 7 | `PREFIX_NAME` | VARCHAR(255) |  |  | The prefix of the personnel's name. |
| 8 | `PRSNL_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of personnel. 1 is a prescriber, 2 is a supervisor. |
| 9 | `STATE_NAME` | VARCHAR(255) |  |  | The personnel's state. |
| 10 | `STREET2_ADDR` | VARCHAR(255) |  |  | The second line of the personnel's address. |
| 11 | `STREET_ADDR` | VARCHAR(255) |  |  | The first line of the personnel's address. |
| 12 | `SUFFIX_NAME` | VARCHAR(255) |  |  | The suffix of the personnel's name. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `ZIP_CODE` | VARCHAR(255) |  |  | The personnel's zip code. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IB_RX_REQ_ID` | [IB_RX_REQ](IB_RX_REQ.md) | `IB_RX_REQ_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [IB_RX_REQ_PRSNL_ALIAS](IB_RX_REQ_PRSNL_ALIAS.md) | `IB_RX_REQ_PRSNL_DEMOG_ID` |
| [IB_RX_REQ_PRSNL_CONTACT](IB_RX_REQ_PRSNL_CONTACT.md) | `IB_RX_REQ_PRSNL_DEMOG_ID` |

