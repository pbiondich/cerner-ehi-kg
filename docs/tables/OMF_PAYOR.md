# OMF_PAYOR

> omf_payor

**Description:** Contains the payor reference data from the OMF Accounts Receivable interface.  
**Table type:** ACTIVITY  
**Primary key:** `OMF_PAYOR_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OMF_PAYOR_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the omf_payor table. |
| 2 | `PAYOR_CODE` | VARCHAR(50) |  |  | An abbreviation for the payor. |
| 3 | `PAYOR_GROUP` | VARCHAR(100) |  |  | A descriptive name that groups payors together for analysis. |
| 4 | `PAYOR_GROUP_CODE` | VARCHAR(50) |  |  | An abbreviation for the payor_group. |
| 5 | `PAYOR_ID` | DOUBLE | NOT NULL |  | The unique identifier for the payor on the organization table. |
| 6 | `PAYOR_NAME` | VARCHAR(100) |  |  | A descriptive name that identifies a party that is responsible to pay this receivable. |
| 7 | `PAYOR_TYPE` | VARCHAR(100) |  |  | A descriptive name that groups payors together for analysis. |
| 8 | `PAYOR_TYPE_CODE` | VARCHAR(50) |  |  | An abbreviation for payor_type. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OMF_ACC_FACT](OMF_ACC_FACT.md) | `OMF_PAYOR_ID` |
| [OMF_ACR_FACT](OMF_ACR_FACT.md) | `OMF_PAYOR_ID` |

