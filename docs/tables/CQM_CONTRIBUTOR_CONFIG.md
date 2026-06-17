# CQM_CONTRIBUTOR_CONFIG

> The CQM contributor configuration table identifies the verifiable alias of contributor applications that are permitted to add transactions to an associated CQM queue table. Each alias is associated with a CQM application in this table.

**Description:** CQM Contributor Configuration  
**Table type:** REFERENCE  
**Primary key:** `CONTRIBUTOR_ID`  
**Columns:** 12  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NAME` | VARCHAR(12) | NOT NULL |  | The application name denotes a specific usage of CQM. This string is limited to twelve characters as it concatenated into DB table names to isolate the physical storage space of transaction by application. |
| 2 | `CONTRIBUTOR_ALIAS` | VARCHAR(48) | NOT NULL |  | The verifiable alias, by application name, which denotes a contributor application that act as the originators of CQM transactions. |
| 3 | `CONTRIBUTOR_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the CQM contributor configuration table. It is an internal system assigned number. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 5 | `DEBUG_IND` | DOUBLE |  |  | Defines whether debugging is active or inactive for the contributor alias and application |
| 6 | `TARGET_PRIORITY` | DOUBLE |  |  | Identifies the priority of a target transaction row in the queue table for the contributor alias and application. The value range for priority is 1 through 99, highest to lowest, respectively. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERBOSITY_FLAG` | DOUBLE |  |  | Defines the verbosity level during debugging for the contributor alias and application. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CQM_BMDI_RESULTS_QUE](CQM_BMDI_RESULTS_QUE.md) | `CONTRIBUTOR_ID` |
| [CQM_FSIESO_QUE](CQM_FSIESO_QUE.md) | `CONTRIBUTOR_ID` |
| [CQM_FSIOCC_QUE](CQM_FSIOCC_QUE.md) | `CONTRIBUTOR_ID` |
| [CQM_MDRESULTS_QUE](CQM_MDRESULTS_QUE.md) | `CONTRIBUTOR_ID` |
| [CQM_MICRESULTS_QUE](CQM_MICRESULTS_QUE.md) | `CONTRIBUTOR_ID` |

