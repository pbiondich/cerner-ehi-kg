# RX_PROTOCOL

> Stores all parameters related to switch and its communication protocols for pharmacy claim processing

**Description:** The rx_protocol file stores all parameters related to switch protocols  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPRESS_IND` | DOUBLE |  |  | Specifies whether or not protocol supports compression (0 is no, 1 is yes) |
| 2 | `CONNECT_PROMPT` | VARCHAR(100) |  |  | This is the prompt string that is sent by the remote switch when a connection is established. |
| 3 | `DIAL_ATTEMPTS` | DOUBLE |  |  | Specifies number of attempts to be made to open a connection to the switch. |
| 4 | `EOM` | VARCHAR(10) |  |  | This is the end of text character that should be appended to the beginning of any message sent using this protocol. |
| 5 | `LRC_IND` | DOUBLE |  |  | Specifies whether or not messages sent using this protocol should have an LRC appended to them (0 is no, 1 is yes) |
| 6 | `MESSAGE_PREFIX` | VARCHAR(15) |  |  | Indicate string prefix to place before each input message |
| 7 | `MESSAGE_PROMPT` | VARCHAR(100) |  |  | This is the prompt that is sent by the remote switch when it is expecting a message. |
| 8 | `OPEN_ATTEMPTS` | DOUBLE |  |  | Specifies number of attempts to be made to open a connection to the network port. |
| 9 | `OPEN_DELAY` | DOUBLE |  |  | Indicates number of seconds within which to send message to keep continuous connection open |
| 10 | `OPEN_PROTOCOL_IND` | DOUBLE |  |  | Indicates whether a this protocol is continuous connection or discrete connection |
| 11 | `PROTOCOL_CD` | DOUBLE | NOT NULL | FK→ | Unique key of file. Assigned Code Set 4542 |
| 12 | `READ_ATTEMPTS` | DOUBLE |  |  | Specifies number of times to attempt to keep reading an incoming message. |
| 13 | `SEND_ATTEMPTS` | DOUBLE |  |  | Specifies number of times the message should be sent before disconnecting when switch negative acknowledges the message. |
| 14 | `SOM` | VARCHAR(10) |  |  | This is the start of text character that should be appended to the beginning of any message sent using this protocol. |
| 15 | `STEP_1` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 16 | `STEP_10` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 17 | `STEP_11` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 18 | `STEP_12` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 19 | `STEP_13` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 20 | `STEP_14` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 21 | `STEP_15` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 22 | `STEP_2` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 23 | `STEP_3` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 24 | `STEP_4` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 25 | `STEP_5` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 26 | `STEP_6` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 27 | `STEP_7` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 28 | `STEP_8` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 29 | `STEP_9` | VARCHAR(100) |  |  | Step to execute for Synchronization |
| 30 | `STRING1` | VARCHAR(30) |  |  | This is the user name |
| 31 | `STRING2` | VARCHAR(30) |  |  | This is the Password |
| 32 | `SYNCHRONIZE_IND` | DOUBLE |  |  | Specifies whether or not this protocol requires a login procedure (0 is no, 1 is yes) |
| 33 | `SYNCH_INIT_CHAR` | VARCHAR(10) |  |  | This is the character required to initiate the logon procedure for this protocol |
| 34 | `SYNCH_STEPS` | DOUBLE |  |  | Number of steps to execute for synchronization. |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 38 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROTOCOL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

