# CQM_FSIESO_QUE

> This CQM queue table is the primary storage locations of the transaction message for the FSI ESO application. This table contains the administrative and routing data used for controlling the transaction.

**Description:** FSI ESO CQM Queue  
**Table type:** ACTIVITY  
**Primary key:** `QUEUE_ID`  
**Columns:** 32  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLASS` | VARCHAR(15) |  |  | Identifies the trigger explosion class of the transaction. |
| 3 | `COMPLETION_SEQ_NBR` | DOUBLE |  |  | Identifies the transaction completion order when being processed by FSI Cloud. |
| 4 | `CONTRIBUTOR_EVENT_DT_TM` | DATETIME |  |  | Significant date and time associated with the transaction row as supplied by the contributor application. |
| 5 | `CONTRIBUTOR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CQM contributor configuration table. It is an internal system assigned number. |
| 6 | `CONTRIBUTOR_REFNUM` | VARCHAR(48) | NOT NULL |  | A reference or key assigned to the transaction row by the contributor application. It recommended that this identifier be unique although it is not required. |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 8 | `CREATE_RETURN_FLAG` | DOUBLE |  |  | The current trigger explosion state for this transaction row. |
| 9 | `CREATE_RETURN_TEXT` | VARCHAR(132) |  |  | Return text string from the trigger explosion process of this transaction row. |
| 10 | `DEBUG_IND` | DOUBLE |  |  | Defines whether debugging is active or inactive for the queue transaction unidentified in this row. |
| 11 | `FSI_CLOUD_FLAG` | DOUBLE |  |  | Indicates whether the transaction is eligible for FSI Cloud processing or not.; Values: 1 = ELIGIBLE for FSI Cloud processing;; 0 = NOT; 2 = TBD |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `LOGICAL_DOMAIN_MNEMONIC` | VARCHAR(100) |  |  | Mnemonic of the logical domain the transaction belongs to. |
| 14 | `MESSAGE` | LONGBLOB |  |  | This is the binary longraw field which contains the contents of the original message. |
| 15 | `MESSAGE_LEN` | DOUBLE | NOT NULL |  | The length of the textual or binary object placed in the message field. |
| 16 | `MESSAGE_SEQUENCE` | DOUBLE | NOT NULL |  | This is a numeric value that determines the order in which the messages will be processed. It is based on the date and time that the row was inserted. |
| 17 | `PARAM_LIST_IND` | DOUBLE |  |  | Identifies whether there are row in the queue parameters table associated with this transaction row. |
| 18 | `PRIORITY` | DOUBLE | NOT NULL |  | Identifies the priority of this transaction row that may or may not be used to process in a prioritized method. The value range for priority is 1 through 99, highest to lowest, respectively. |
| 19 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | The current trigger explosion state for this transaction row. |
| 20 | `QUEUE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 21 | `SUBTYPE` | VARCHAR(15) |  |  | Identifies the trigger explosion subtype of the transaction. |
| 22 | `SUBTYPE_DETAIL` | VARCHAR(15) |  |  | Identifies the trigger explosion subtype detail of the transaction. |
| 23 | `TRIG_CREATE_END_DT_TM` | DATETIME |  |  | The date and time the trigger explosion completed on this transaction row. |
| 24 | `TRIG_CREATE_START_DT_TM` | DATETIME |  |  | The date and time the trigger explosion began on this transaction row. |
| 25 | `TRIG_MODULE_IDENTIFIER` | VARCHAR(16) |  |  | Future. Identifies the process/module which performs the trigger explosion on this transaction row. |
| 26 | `TYPE` | VARCHAR(15) |  |  | Identifies the trigger explosion type of the transaction. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VERBOSITY_FLAG` | DOUBLE |  |  | Defines the verbosity level during debugging for the processing of the transaction. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_ID` | [CQM_CONTRIBUTOR_CONFIG](CQM_CONTRIBUTOR_CONFIG.md) | `CONTRIBUTOR_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [DQR_DOCUMENT_ACTION](DQR_DOCUMENT_ACTION.md) | `ESO_QUEUE_ID` |
| [FSIESO_QUE_DETAILS](FSIESO_QUE_DETAILS.md) | `QUEUE_ID` |
| [HOLD_QUEUE](HOLD_QUEUE.md) | `QUEUE_ID` |
| [SI_AUDIT](SI_AUDIT.md) | `QUEUE_ID` |
| [WF_STFG_HDR](WF_STFG_HDR.md) | `QUEUE_ID` |

